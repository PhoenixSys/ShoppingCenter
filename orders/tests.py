from django.test import TestCase

# Create your tests here.
from customers.models import Costumers
from orders.models import Order, OrderItem
from products.models import Discount, Products, Categories


class TestProductDiscount(TestCase):
    def setUp(self):
        self.costumer1 = Costumers.objects.create(username="phoenix", password="1234", f_name="mobin", l_name="atashi",
                                                  phone="626426246", email="mobinatashi2@gmail.com")
        self.discount1 = Discount.objects.create(value=20, type='percent')
        self.discount2 = Discount.objects.create(value=5000, type='price')
        self.discount3 = Discount.objects.create(value=30, type='percent', max_price='10000')
        self.discount3 = Discount.objects.create(value=30, type='percent')
        self.category1 = Categories.objects.create(type="Electronic")
        self.category2 = Categories.objects.create(type="Mobile", discount=self.discount2)
        inst1 = self.product1 = Products.objects.create(name="Samsung A12", price=20000,
                                                        discount=self.discount1, description="")
        inst1.category.set([self.category2])
        inst2 = self.product2 = Products.objects.create(name="Samsung A12", price=20000,
                                                        discount=self.discount2, description="")
        inst2.category.set([self.category2, self.category1])
        self.order1 = Order.objects.create(costumer=self.costumer1, status=1)
        self.item_order1 = OrderItem.objects.create(order=self.order1, item=self.product1)
        self.item_order2 = OrderItem.objects.create(order=self.order1, item=self.product2)

    def test_FinalPriceProduct(self):
        print(self.order1.get_total_cost)
