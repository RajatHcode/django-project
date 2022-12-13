from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class FileUpload(models.Model):
    file = models.FileField(_("File"), blank=False, null=False)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = _("Uploaded File")
        verbose_name_plural = _("Uploaded Files")
