from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile, Notification
from ..forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def list_user_offers(request):
	offers = Offer.objects.filter()
	my_offers = [offer for offer in offers if (offer.book.owner == request.user) and (offer.active == True)]
	return render(request, 'tradingsystem/my_offers.html', {'offers': my_offers, 'len':len(my_offers)})

@login_required
def offer_info(request):
    offer_id = request.GET.get('id')
    offer = Offer.objects.filter(id=offer_id)
    offer = offer[0]
    ad = offer.offered_to

    rejected = False
    accepted = False
    canceled = False

    if request.method == 'POST':
        if 'accept' in request.POST:
            ad.active = False
            offer.active = False
            ad.save()
            offer.save()

            trade = Trade()
            trade.ad = ad
            trade.offer = offer
            trade.advertiser = ad.book.owner
            trade.offeror = offer.book.owner
            trade.save()
            trade.notify()

            ad_book = Book.objects.filter(id=ad.book.id)
            offer_book = Book.objects.filter(id=offer.book.id)
            ad_book = ad_book[0]
            offer_book = offer_book[0]

            ad_book.owner = trade.offeror
            offer_book.owner = trade.advertiser
            ad_book.save()
            offer_book.save()

            offers_to_ad = ad.offers.all()
            for o in offers_to_ad:
                if o.active == True:
                    o.active = False
                    o.notify_offer_rejected()
                    o.save()

            accepted = True

        elif 'reject' in request.POST:
            ad.offers.remove(offer)
            ad.save()
            offer.active = False
            offer.save()
            rejected = True
            offer.notify_offer_rejected()

        elif 'cancel' in request.POST:
            ad.offers.remove(offer)
            ad.save()
            offer.active = False
            offer.save()
            canceled = True

    return render(request, "tradingsystem/offer_info.html", {'offer': offer,
                                                             'ad': ad,
                                                             'rejected': rejected,
                                                             'accepted': accepted,
                                                             'canceled': canceled})

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

        ads = Ad.objects.filter(book=book, active=True)
        offers = Offer.objects.filter(book=book, active=True)
        if len(ads) != 0 or len(offers) != 0:
            error = True
        else:
            offer.book = book;
            offer.city = request.POST['city']
            offer.offered_to = ad
            offer.active = True
            offer.save()
            offer.notify_offer_proposed()
            ad.offers.add(offer)
            ad.save()
            success = True

    return render(request, 'tradingsystem/offer_trade.html', {  'ad': ad, 
                                                                'books': user_books,
                                                                'user_city': user_profile.city,
                                                                'success': success,
                                                                'error': error,
                                                                'form': form})