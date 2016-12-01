from django.conf.urls import include, url
from tradingsystem import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/?$', views.register_user),
    url(r'^login/?$', views.user_login, name='login'),
    url(r'^logout/?$', views.user_logout),
    url(r'^index/?$', views.index),
    url(r'^search/?$', views.search),
    url(r'^add_book/?$', views.add_book),
    url(r'^book_list/?$', views.book_list),
    url(r'^book_info/?$', views.book_info),
    url(r'^my_books/?$', views.list_user_book),
    url(r'^advertise/?$', views.create_ad),
    url(r'^my_ads/?$', views.list_user_ads),
    url(r'^offer_trade/?$', views.offer_trade),
    url(r'^offer_info/?$', views.offer_info),
    url(r'^my_offers/?$', views.list_user_offers),
]
