from django.db import models
from django.contrib.auth.models import User
import uuid

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
    user = models.OneToOneField(User)
    address = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.username

    
