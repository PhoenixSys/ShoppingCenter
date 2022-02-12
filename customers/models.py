from django.db import models

# Create your models here.
from core.models import BaseModel


class Addresses(BaseModel):
    costumer = models.ForeignKey("Costumers", on_delete=models.RESTRICT)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    postal_code = models.IntegerField()


class Costumers(BaseModel):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    f_name = models.CharField(max_length=64)
    l_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16, unique=True)
    email = models.CharField(max_length=64, unique=True)
