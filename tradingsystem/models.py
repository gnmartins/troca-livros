from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

    def notify_offer_proposed(self):
        notification = Notification()
        notification.user = self.offered_to.book.owner
        notification.message = "Recebida oferta em troca do livro '%s' de %s" % (self.offered_to.book.title, self.book.owner)
        notification.save()
    
    def notify_offer_rejected(self):
        notification = Notification()
        notification.user = self.book.owner
        notification.message = "Sua oferta em troca do livro '%s' de %s foi rejeitada." % (self.offered_to.book.title, self.offered_to.book.owner)
        notification.save()


class Trade(models.Model):
    ad = models.ForeignKey('Ad');
    offer = models.ForeignKey('Offer');
    advertiser = models.ForeignKey('auth.User', related_name='trade_advertiser', null=True)
    offeror = models.ForeignKey('auth.User', related_name='trade_offeror', null=True)
    date = models.DateTimeField(default=timezone.now)

    def notify(self):
        notification = Notification()
        notification.user = self.offeror
        notification.message = "Sua oferta em troca do livro '%s' de %s foi aceita." % (self.ad.book.title, self.advertiser)
        notification.save()


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

class Notification(models.Model):
    user = models.ForeignKey('auth.User')
    message = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now)