from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from book_app.constants import UserType
# Create your models here.

# User type


class UserProfile(models.Model):
    type = models.CharField(choices=UserType.choices, max_length=15,
                            default=UserType.READER, null=False, blank=False)
    name = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(
        User, null=False, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    edition = models.IntegerField()
    author = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    link = models.URLField(max_length=50, null=True)

    def __str__(self):
        return self.name
