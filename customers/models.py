from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from core.models import BaseModel


class Addresses(BaseModel):
    costumer = models.ForeignKey("Costumers", on_delete=models.RESTRICT, verbose_name=_("Costumer"))
    state = models.CharField(max_length=64, verbose_name=_("State"))
    city = models.CharField(max_length=64, verbose_name=_("City"))
    postal_code = models.IntegerField(unique=True, verbose_name=_("PostalCode"))

    def __str__(self):
        return f"Costumer : {self.costumer} | City : {self.city}"


class Costumers(BaseModel):
    username = models.CharField(max_length=64, unique=True, verbose_name=_("Username"))
    password = models.CharField(max_length=64, verbose_name=_("Password"))
    f_name = models.CharField(max_length=64, verbose_name=_("First Name"))
    l_name = models.CharField(max_length=64, verbose_name=_("Last Name"))
    phone = models.CharField(max_length=16, unique=True, verbose_name=_("Phone"))
    email = models.CharField(max_length=64, unique=True, validators=[EmailValidator], verbose_name=_("Email"))

    def __str__(self):
        return f"Username : {self.username} | Phone : {self.phone}"
