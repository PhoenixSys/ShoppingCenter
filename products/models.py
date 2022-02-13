# Create your models here.
from django.db import models
from core.models import BaseModel


class Products(BaseModel):
    name = models.CharField(max_length=64)
    category = models.ManyToManyField("Categories")
    price = models.IntegerField()
    discount = models.ForeignKey("Discount", on_delete=models.RESTRICT, null=True, blank=True)
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField()

    def __str__(self):
        return f"{self.name} | {self.category} | {self.price}"


#
class Categories(BaseModel):
    type = models.CharField(max_length=64)
    discount = models.ForeignKey("Discount", on_delete=models.RESTRICT, null=True, blank=True)
    parent = models.ForeignKey(
        "Categories", related_name="categories", null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Type : {self.type} | Parent : {self.parent}"


class Discount(BaseModel):
    type = models.CharField(max_length=64)
    value = models.IntegerField()
    code = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f"Type : {self.type} | Value : {self.value} | Code : {self.code}"
