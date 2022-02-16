# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.db import models
from core.models import BaseModel


class Products(BaseModel):
    name = models.CharField(max_length=64, unique=True, verbose_name=_("Name"))
    category = models.ManyToManyField("Categories", verbose_name=_("Category"))
    price = models.IntegerField(verbose_name=_("Price"))
    discount = models.ForeignKey("Discount", on_delete=models.RESTRICT, null=True, blank=True,
                                 verbose_name=_("Discount"))
    image = models.ImageField(upload_to="uploads/", null=True, blank=True, verbose_name=_("Image"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))

    def final_price(self):
        final_prices = (self.price - self.discount.profit_value(self.price)) if self.discount else self.price
        self.final_price = final_prices
        return final_prices

    def __str__(self):
        return f"{self.name} | {self.category} | {self.price}"


class Categories(BaseModel):
    type = models.CharField(max_length=64, verbose_name=_("Type"))
    discount = models.ForeignKey("Discount", on_delete=models.RESTRICT, null=True, blank=True,
                                 verbose_name=_("Discount"))
    parent = models.ForeignKey(
        "Categories", related_name="categories", null=True, blank=True, on_delete=models.CASCADE
        , verbose_name=_("Parent"))

    def __str__(self):
        return f"Type : {self.type} | Parent : {self.parent}"


class Discount(BaseModel):
    type = models.CharField(max_length=10, choices=[
        ('price', 'Price'), ('percent', 'Percent')
    ], null=False, verbose_name=_("Type"))
    value = models.PositiveIntegerField(verbose_name=_("Value"))
    max_price = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Max_Price"))

    def profit_value(self, price: int):
        if self.type == 'price':
            return min(self.value, price)
        else:
            raw_profit = int((self.value / 100) * price)
            return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit

    def __str__(self):
        return f"Type : {self.type} | Value : {self.value}"
