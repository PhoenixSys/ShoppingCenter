from django.db import models
# Create your models here.
from model_utils import Choices
from core.models import BaseModel
from customers.models import Costumers
from products.models import Products

ORDER_STATUS = Choices(
    (0, 'CANCEL', 'Cancel'),
    (1, 'UNPAID', 'Unpaid'),
    (2, 'PAIN', 'Paid'),
)


class Order(BaseModel):
    costumer = models.ForeignKey(Costumers, on_delete=models.RESTRICT)
    status = models.IntegerField(choices=ORDER_STATUS, default=ORDER_STATUS.UNPAID, verbose_name='Status')
    is_paid = models.BooleanField(default=False, verbose_name='Paid')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id} status :{self.status} '

    @property
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} * {self.item.name}"

    # @property
    # def get_cost(self):
    #     return (self.item.price - self.item.discount) * self.quantity
