from django.core.validators import EmailValidator
from django.db import models

# Create your models here.
from core.models import BaseModel


class Addresses(BaseModel):
    costumer = models.ForeignKey("Costumers", on_delete=models.RESTRICT)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    postal_code = models.IntegerField()

    def __str__(self):
        return f"Costumer : {self.costumer} | City : {self.city}"


class Costumers(BaseModel):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    f_name = models.CharField(max_length=64)
    l_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16, unique=True)
    email = models.CharField(max_length=64, unique=True, validators=[EmailValidator])

    def __str__(self):
        return f"Username : {self.username} | Phone : {self.phone}"
