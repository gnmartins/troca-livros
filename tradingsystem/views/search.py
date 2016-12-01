from django.shortcuts import render
from django import template
from ..models import Book, Ad, Offer, Trade, UserProfile
from ..forms import AddBookForm, SearchBookForm, UserForm, UserProfileForm, CreateAdForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Search related views

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
            ads = Ad.objects.filter()
            
            s_ads = [ad for ad in ads if ad.book in s_results and ad.active == True]
            length = len(s_ads)


            return render(request, 'tradingsystem/ad_list.html', {'ads': s_ads, 'len': length})
    else:
        form = SearchBookForm(empty_permitted=True)

    return render(request, 'tradingsystem/search.html', {'form': form,})
