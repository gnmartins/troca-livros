from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile
from ..forms import AddBookForm, SearchBookForm, UserForm, UserProfileForm, CreateAdForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Book related views

@login_required
def book_list(request):
	books = Book.objects.all()
	return render(request, 'tradingsystem/book_list.html', {'books': books})

@login_required
def book_info(request):
	if request.method == 'GET':
		book_id = request.GET.get('id')
		book = Book.objects.filter(id=book_id)
		book = list(book[:1])[0]
		return render(request, 'tradingsystem/book_info.html', {'book': book})

@login_required
def add_book(request):
	form = AddBookForm(request.POST)
	book = Book();
	success = False;
	if form.is_valid():
		book.owner 		  = request.user
		book.title 		  = request.POST['title']
		book.author 	  = request.POST['author']
		book.publisher 	  = request.POST['publisher']
		book.year 		  = request.POST['year']
		book.isbn		  = request.POST['isbn']
		book.conservation = request.POST['conservation']
		book.save()
		success = True;
	return render(request, 'tradingsystem/add_book.html', {'form':form, 'success': success})

@login_required
def list_user_book(request):
    books = Book.objects.filter(owner=request.user)
    return render(request,'tradingsystem/my_books.html', {'books':books})