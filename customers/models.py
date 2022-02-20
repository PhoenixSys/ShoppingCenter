from django.core.validators import EmailValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from core.models import BaseModel, User


class Addresses(BaseModel):
    costumer = models.ForeignKey("Costumers", on_delete=models.CASCADE, verbose_name=_("Costumer"))
    state = models.CharField(max_length=64, verbose_name=_("State"))
    city = models.CharField(max_length=64, verbose_name=_("City"))
    postal_code = models.IntegerField(unique=True, verbose_name=_("PostalCode"))
    optional = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return f"Costumer : {self.costumer} | City : {self.city}"


class Costumers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_address = models.OneToOneField(Addresses, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Costumer")
        verbose_name_plural = _("Costumers")

    def __str__(self):
        return f"Username : {self.user.username} | Phone : {self.user.phone}"
