from django import forms
from django.contrib.auth.models import User
from .models import Book, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address', )

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'year', 'isbn', 'conservation')

class SearchBookForm(forms.Form):
    title = forms.CharField(max_length=200, required=False)
    author = forms.CharField(max_length=200, required=False)
    publisher = forms.CharField(max_length=200, required=False)
    year = forms.CharField(max_length=200, required=False)
    isbn = forms.CharField(max_length=200, required=False)



