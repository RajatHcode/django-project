from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserType(models.TextChoices):
    AUTHOR = "AUTHOR", _("Author")
    READER = "READER", _("Reader")
