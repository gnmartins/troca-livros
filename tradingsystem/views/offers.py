from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile
from ..forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def offer_trade(request):
    
    # user info
    user_profile = UserProfile.objects.filter(user=request.user)
    user_profile = user_profile[0]
    
    #if request.method == 'GET':
    # ad being visualized  
    ad_id = request.GET.get('id')
    ad = Ad.objects.filter(id=ad_id)
    ad = ad[0]

    form = OfferTradeForm(request.POST, initial={"city": user_profile.city,
                                                 "offered_to": ad})

    # user books
    user_books = Book.objects.filter(owner=request.user)

    success = False
    error = False
    offer = Offer()
    
    if form.is_valid():
        book_id = request.POST['book']
        book = Book.objects.filter(id=book_id)
        book = book[0]

        ads = Ad.objects.filter(book=book)
        offers = Offer.objects.filter(book=book)
        if len(ads) != 0 or len(offers) != 0:
            error = True
        else:
            offer.book = book;
            offer.city = request.POST['city']
            offer.offered_to = ad
            offer.save()
            ad.offers.add(offer)
            ad.save()
            success = True

    return render(request, 'tradingsystem/offer_trade.html', {  'ad': ad, 
                                                                'books': user_books,
                                                                'user_city': user_profile.city,
                                                                'success': success,
                                                                'error': error,
                                                                'form': form})