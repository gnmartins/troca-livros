from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/?$', views.index),
    url(r'^search/?$', views.search),
    url(r'^add_book/?$', views.add_book),
    url(r'^book_list/?$', views.book_list),
    url(r'^book_info/?$', views.book_info),
]