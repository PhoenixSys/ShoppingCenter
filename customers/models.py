from django.core.validators import EmailValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from core.models import BaseModel


class Addresses(BaseModel):
    costumer = models.ForeignKey("Costumers", on_delete=models.RESTRICT, verbose_name=_("Costumer"))
    state = models.CharField(max_length=64, verbose_name=_("State"))
    city = models.CharField(max_length=64, verbose_name=_("City"))
    postal_code = models.IntegerField(unique=True, verbose_name=_("PostalCode"))

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return f"Costumer : {self.costumer} | City : {self.city}"


class Costumers(BaseModel):
    username = models.CharField(max_length=64, unique=True, verbose_name=_("Username"))
    password = models.CharField(max_length=64, verbose_name=_("Password"))
    f_name = models.CharField(max_length=64, verbose_name=_("First Name"))
    l_name = models.CharField(max_length=64, verbose_name=_("Last Name"))
    phone = models.CharField(max_length=11, unique=True, verbose_name=_("Phone"),
                             validators=[RegexValidator(regex="^(9|(09))(((1)|(3))([0-9])|(20)|(21))(\d{7})",
                                                       message="Phone Number Is Not Valid")])
    email = models.EmailField(max_length=64, unique=True, validators=[EmailValidator], verbose_name=_("Email"))

    class Meta:
        verbose_name = _("Costumer")
        verbose_name_plural = _("Costumers")

    def __str__(self):
        return f"Username : {self.username} | Phone : {self.phone}"
