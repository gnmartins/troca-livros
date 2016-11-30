from django.db import models
from django.contrib.auth.models import User
import uuid

class Offered(models.Model):
    book = models.Book;
    city = models.CharField(max_length=200)

class Trade(models.Model):
    offer = models.Offer;
    offered = models.Offered;
    emailOffer = models.CharField(max_length=200)
    emailOffered = models.CharField(max_length=200)


class Offer(models.Model):
    book = models.Book;
    city = models.CharField(max_length=200)



class Book(models.Model):

    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    conservation = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    def save(self):
        super(Book, self).save()
        #print(self.id)


class UserProfile(models.Model):
    user    = models.OneToOneField(User)
    address = models.CharField(max_length=200)
    email   = models.CharField(max_length=200)
    city    = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.username

    
