from django.shortcuts import render
from .models import Book
from .forms import AddBookForm

# Create your views here.

def book_list(request):
	return render(request, 'tradingsystem/book_list.html', {})

def addBook(request):
	form = AddBookForm(request.POST)
	if form.is_valid():
		newBook.author 		= form.author
		newBook.title 		= form.title
		newBook.publisher 	= form.publisher
		newBook.year	  	= form.year
		newBook.isbn	  	= form.isbn
	return render(request, 'tradingsystem/addBook.html', {'form':form})
	