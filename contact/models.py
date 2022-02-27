from django.db import models

# Create your models here.
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class ContactUs(BaseModel):
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    text = models.TextField(verbose_name=_("Text"))

    class Meta:
        verbose_name = _("ContactUs")
        verbose_name_plural = _("ContactUs")

    def __str__(self):
        return f"{self.name} | {self.email} | {self.text}"
