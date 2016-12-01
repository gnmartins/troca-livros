from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile, Notification
from ..forms import AddBookForm, SearchBookForm, UserForm, UserProfileForm, CreateAdForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Basic views

def index(request):
	notifications = []
	if request.user.is_authenticated:
		notifications = Notification.objects.filter(user=request.user).order_by('date')

		if request.method == 'POST':
			notifications.delete()

	return render(request, 'tradingsystem/index.html', {'notifications': notifications})