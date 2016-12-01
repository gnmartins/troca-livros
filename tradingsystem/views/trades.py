from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile
from ..forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def list_user_trades(request):

    return render(request, "tradingsystem/offer_info.html", {'trades': trades})