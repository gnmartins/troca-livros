from django.shortcuts import render
from .models import Book
from .forms import AddBookForm, SearchBookForm

# Create your views here.

def index(request):
	return render(request, 'tradingsystem/index.html', {})

def book_list(request):
	books = Book.objects.all()
	return render(request, 'tradingsystem/book_list.html', {'books': books})

def addBook(request):
	form = AddBookForm(request.POST)
	if form.is_valid():
		newBook = form.save()
		newBook.save()
	return render(request, 'tradingsystem/addBook.html', {'form':form})
	
def search(request):
	if request.method == 'POST':
		form = SearchBookForm(request.POST)
		if form.is_valid():
			s_query = form.cleaned_data['title']
			s_results = Book.objects.filter(title = s_query)
			return render(request, 'tradingsystem/book_list.html', {'books': s_results})
	else:
		form = SearchBookForm()

	return render(request, 'tradingsystem/search.html', {'form': form,})