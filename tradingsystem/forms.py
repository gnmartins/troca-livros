from django import forms

from .models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('owner','title', 'author', 'publisher', 'year', 'isbn')

class SearchBookForm(forms.Form):
    title = forms.CharField(max_length=200, required=False)
    author = forms.CharField(max_length=200, required=False)
    publisher = forms.CharField(max_length=200, required=False)
    year = forms.CharField(max_length=200, required=False)
    isbn = forms.CharField(max_length=200, required=False)

