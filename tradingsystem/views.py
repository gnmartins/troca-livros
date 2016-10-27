from django.shortcuts import render
from .models import Book
from .forms import AddBookForm, SearchBookForm

# Create your views here.

def index(request):
	return render(request, 'tradingsystem/index.html', {})

def book_list(request):
	books = Book.objects.all()
	return render(request, 'tradingsystem/book_list.html', {'books': books})

def book_info(request):
	if request.method == 'GET':
		book_id = request.GET.get('id')
		book = Book.objects.filter(id=book_id)
		book = list(book[:1])[0]
		return render(request, 'tradingsystem/book_list.html', {'books': [book]})

def add_book(request):
	form = AddBookForm(request.POST)
	if form.is_valid():
		newBook = form.save()
		newBook.save()
	return render(request, 'tradingsystem/add_book.html', {'form':form})
	
def search(request):
	if request.method == 'POST':
		form = SearchBookForm(request.POST)
		if form.is_valid():
			fields = {}
			fields['title']     = form.cleaned_data['title']
			fields['author']    = form.cleaned_data['author']
			fields['publisher'] = form.cleaned_data['publisher']
			fields['year']      = form.cleaned_data['year']
			fields['isbn']      = form.cleaned_data['isbn']

			arguments = {}
			for k, v in fields.items():
				if len(v) > 0:
					arguments[k] = v

			s_results = Book.objects.filter(**arguments)
			length = len(s_results)	
			return render(request, 'tradingsystem/book_list.html', {'books': s_results, 'len': length})
	else:
		form = SearchBookForm(empty_permitted=True)

	return render(request, 'tradingsystem/search.html', {'form': form,})