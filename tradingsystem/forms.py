from django import forms

from .models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('owner','title', 'author', 'publisher', 'year', 'isbn')

class SearchBookForm(forms.Form):
    title = forms.CharField(max_length=200)

