from django.db import models
from django.contrib.auth.models import User
import uuid

class Ad(models.Model):
    book = models.ForeignKey('Book');
    city = models.CharField(max_length=200)
    offers = models.ManyToManyField('Offer')
    active = models.BooleanField()

class Offer(models.Model):
    book = models.ForeignKey('Book');
    city = models.CharField(max_length=200)
    offered_to = models.ForeignKey('Ad')
    active = models.BooleanField()

class Trade(models.Model):
    ad = models.ForeignKey('Ad');
    offer = models.ForeignKey('Offer');
    emailAdvertiser = models.CharField(max_length=200)
    emailOfferor = models.CharField(max_length=200)
    active = models.BooleanField()

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
    

class UserProfile(models.Model):
    user    = models.OneToOneField(User)
    address = models.CharField(max_length=200)
    city    = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.username

    
