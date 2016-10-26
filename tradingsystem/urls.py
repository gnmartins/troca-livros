from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.book_list),
    url(r'^addBook$', views.addBook),
]