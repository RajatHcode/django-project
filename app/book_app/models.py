from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from book_app.constants import UserType
# Create your models here.

# User Profile Model


class UserProfile(models.Model):
    type = models.CharField(_("User Type"), choices=UserType.choices, max_length=15,
                            default=UserType.READER, null=False, blank=False)
    name = models.CharField(_("Name"), max_length=50, null=False, blank=False)
    location = models.CharField(
        _("Location"), max_length=30, blank=False, null=False)

    birth_date = models.DateField(_("Date Of Birth"), null=False, blank=False)
    user = models.OneToOneField(
        User, null=False, blank=False, on_delete=models.DO_NOTHING)

    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")


# Book Model

class Book(models.Model):
    name = models.CharField(_("Name"), max_length=100, null=False, blank=False)
    price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)
    edition = models.IntegerField(_("Edition"), default=1, validators=[
                                  MinValueValidator(1), MaxValueValidator(20)])
    author = models.ForeignKey(
        UserProfile, null=False, blank=False, on_delete=models.DO_NOTHING)
    link = models.URLField(max_length=50, null=False, blank=False)

    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
