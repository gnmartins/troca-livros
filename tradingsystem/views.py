from django.shortcuts import render
from .models import Book
from .forms import AddBookForm

# Create your views here.

def book_list(request):
	books = Book.objects.all()
	return render(request, 'tradingsystem/book_list.html', {'books': books})

def addBook(request):
	form = AddBookForm(request.POST)
	if form.is_valid():
		newBook = form.save()
		newBook.save()
	return render(request, 'tradingsystem/addBook.html', {'form':form})
	