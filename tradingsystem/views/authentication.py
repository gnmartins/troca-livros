from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile
from ..forms import AddBookForm, SearchBookForm, UserForm, UserProfileForm, CreateAdForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def register_user(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			registered = True
		
		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'tradingsystem/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('index')
			else:
				return HttpResponse('Account disabled.')
		else:
			print("Login invalido: {0}, {1}".format(username, password))
			return render(request, 'tradingsystem/login.html', {'invalid': True})
		
	else:
		return render(request, 'tradingsystem/login.html', {'invalid': False})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('index')