from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile
from ..forms import AddBookForm, SearchBookForm, UserForm, UserProfileForm, CreateAdForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Ad related views

@login_required
def list_user_ads(request):
	ads = Ad.objects.filter()
	my_ads = [ad for ad in ads if (ad.book.owner == request.user) and (ad.active == True)]
	return render(request, 'tradingsystem/my_ads.html', {'ads': my_ads, 'len':len(my_ads)})

@login_required
def create_ad(request):
	user_profile = UserProfile.objects.filter(user=request.user)
	user_profile = user_profile[0]

	form = CreateAdForm(request.POST, initial={"city": user_profile.city})
	ad = Ad();
	success = False
	error = False
	user_books = Book.objects.filter(owner=request.user)

	if form.is_valid():
		book_id = request.POST['book']
		book = Book.objects.filter(id=book_id)
		book = book[0]

		ads = Ad.objects.filter(book=book, active=True)
		offers = Offer.objects.filter(book=book, active=True)
		if len(ads) != 0 or len(offers) != 0:
			error = True
		else:
			ad.book = book
			ad.city = request.POST['city']
			ad.active = True
			ad.save()
			success = True

	return render(request, 'tradingsystem/create_ad.html', {'form':form, 
															'success': success, 
															'books': user_books,
															'user_city': user_profile.city,
															'error': error})

 
