from django.db import models
# Create your models here.
from core.models import BaseModel
from customers.models import Costumers
from products.models import Products


class Orders(BaseModel):
    costumer = models.ForeignKey(Costumers, on_delete=models.RESTRICT)
    item = models.ForeignKey(Products, on_delete=models.RESTRICT)
    item_count = models.IntegerField()
    status = models.CharField(max_length=32,
                              choices=(("waiting", "wait for accept admin"), ("sending", "sending to costumer"),
                                       ("received", "received to costumer")))
