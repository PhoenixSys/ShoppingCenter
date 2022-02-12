# Create your models here.
from django.db import models

from core.models import BaseModel


class Products(BaseModel):
    name = models.CharField(max_length=64)
    category = models.ForeignKey("Categories", on_delete=models.RESTRICT)
    price = models.IntegerField()
    discount = models.ForeignKey("Discount", on_delete=models.RESTRICT)
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField()


class Categories(BaseModel):
    type = models.CharField(max_length=64)
    discount = models.ForeignKey("Discount", on_delete=models.RESTRICT)


class Discount(BaseModel):
    type = models.CharField(max_length=64)
    value = models.IntegerField()
    code = models.CharField(max_length=64, null=True, blank=True)
