from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile
from ..forms import AddBookForm, SearchBookForm, UserForm, UserProfileForm, CreateAdForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Basic views

def index(request):
	if request.user.is_authenticated:
		"""Lógica das notificações"""
	return render(request, 'tradingsystem/index.html', {})