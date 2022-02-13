# Create your models here.
from django.db import models
from core.models import BaseModel


class Products(BaseModel):
    name = models.CharField(max_length=64)
    category = models.ManyToManyField("Categories")
    price = models.IntegerField()
    discount = models.ForeignKey("Discount", on_delete=models.RESTRICT, null=True, blank=True)
    image = models.ImageField(upload_to="uploads/" , null=True , blank=True)
    description = models.TextField()

    def final_price(self):
        final_prices = self.price - self.discount.profit_value(self.price) if self.discount else self.price
        self.final_price = final_prices
        return final_prices

    def __str__(self):
        return f"{self.name} | {self.category} | {self.price}"


class Categories(BaseModel):
    type = models.CharField(max_length=64)
    discount = models.ForeignKey("Discount", on_delete=models.RESTRICT, null=True, blank=True)
    parent = models.ForeignKey(
        "Categories", related_name="categories", null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Type : {self.type} | Parent : {self.parent}"


class Discount(BaseModel):
    type = models.CharField(max_length=10, choices=[
        ('price', 'Price'), ('percent', 'Percent')
    ], null=False)
    value = models.PositiveIntegerField()
    code = models.CharField(max_length=64, null=True, blank=True)
    max_price = models.PositiveIntegerField(null=True, blank=True)

    def profit_value(self, price: int):
        if self.type == 'price':
            return min(self.value, price)
        else:
            raw_profit = int((self.value / 100) * price)
            return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit

    def __str__(self):
        return f"Type : {self.type} | Value : {self.value} | Code : {self.code}"
