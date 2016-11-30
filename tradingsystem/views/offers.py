from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile
from ..forms import AddBookForm, SearchBookForm, UserForm, UserProfileForm, CreateAdForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def offer_trade(request):
    if request.method == 'GET':
        user_profile = UserProfile.objects.filter(user=request.user)
        user_profile = user_profile[0]

        ad_id = request.GET.get('id')
        ad = Ad.objects.filter(id=ad_id)
        ad = ad[0]

        user_books = Book.objects.filter(owner=request.user)

        return render(request, 'tradingsystem/offer_trade.html', {'ad': ad, 
                                                                  'books': user_books,
                                                                  'user_city': user_profile.city})