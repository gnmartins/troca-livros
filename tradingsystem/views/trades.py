from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile
from ..forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def list_user_trades(request):
    ads = Trade.objects.filter(advertiser=request.user)
    offers = Trade.objects.filter(offeror=request.user)
    
    ads.reverse()
    offers.reverse()

    return render(request, "tradingsystem/my_trades.html", {'ads': ads,
                                                            'offers': offers,})