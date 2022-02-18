from django.db import models
# Create your models here.
from model_utils import Choices
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from customers.models import Costumers, Addresses
from products.models import Products

ORDER_STATUS = Choices(
    (0, 'CANCEL', 'Cancel'),
    (1, 'UNPAID', 'Unpaid'),
    (2, 'PAIN', 'Paid'),
)


class Order(BaseModel):
    costumer = models.ForeignKey(Costumers, on_delete=models.RESTRICT, verbose_name=_("Costumers"))
    address = models.ForeignKey(Addresses, on_delete=models.RESTRICT, verbose_name=_("Address"))
    status = models.IntegerField(choices=ORDER_STATUS, default=ORDER_STATUS.UNPAID, verbose_name=_('Status'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Paid'))

    class Meta:
        ordering = ('-created',)
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f'Order {self.id} status :{self.status} '

    @property
    def get_total_cost(self):
        return sum(item.get_cost for item in self.order_items.all())


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE, verbose_name=_("Order"))
    item = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name=_("Item"))
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = _("OrderItem")
        verbose_name_plural = _("OrderItems")

    def __str__(self):
        return f"{self.quantity} * {self.item.name}"

    @property
    def get_cost(self):
        return (self.item.final_price()) * self.quantity
