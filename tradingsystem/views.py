from django.shortcuts import render
from .models import Book
from .forms import AddBookForm, SearchBookForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
	return render(request, 'tradingsystem/index.html', {})

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

@login_required
def search(request):
	if request.method == 'POST':
		form = SearchBookForm(request.POST)
		if form.is_valid():
			fields = {}
			fields['title__contains']     = form.cleaned_data['title']
			fields['author__contains']    = form.cleaned_data['author']
			fields['publisher__contains'] = form.cleaned_data['publisher']
			fields['year__contains']      = form.cleaned_data['year']
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
