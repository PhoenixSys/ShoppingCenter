from django.test import TestCase

# Create your tests here.
from core.models import User
from customers.models import Costumers, Addresses
from orders.models import Order, OrderItem
from products.models import Discount, Products, Categories


class TestProductDiscount(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(phone="09142520208", password="admin", email="mobinatashi2@gmail.com")
        self.costumer1 = Costumers.objects.create(user=self.user1)
        self.address1 = Addresses.objects.create(costumer=self.costumer1, state="sharghi", city="tabriz",
                                                 postal_code=1234567)
        self.costumer1.default_address = self.address1
        self.costumer1.save()
        self.discount1 = Discount.objects.create(value=20, type='percent')
        self.discount2 = Discount.objects.create(value=5000, type='price')
        self.discount3 = Discount.objects.create(value=30, type='percent', max_price='10000')
        self.discount3 = Discount.objects.create(value=30, type='percent')
        self.category1 = Categories.objects.create(type="Electronic")
        self.category2 = Categories.objects.create(type="Mobile")
        inst1 = self.product1 = Products.objects.create(name="Samsung A12", price=20000,
                                                        discount=self.discount1, description="")
        inst1.category.set([self.category2])
        inst2 = self.product2 = Products.objects.create(name="Samsung A12s", price=20000,
                                                        discount=self.discount2, description="")
        inst2.category.set([self.category2, self.category1])
        self.order1 = Order.objects.create(costumer=self.costumer1, status=1)
        self.item_order1 = OrderItem.objects.create(order=self.order1, item=self.product1)
        self.item_order2 = OrderItem.objects.create(order=self.order1, item=self.product2)
        self.order2 = Order.objects.create(costumer=self.costumer1, status=1)
        self.item_order3 = OrderItem.objects.create(order=self.order2, item=self.product1)

    def test_FinalPriceProduct(self):
        self.assertEqual(self.order1.get_total_cost, 31000)
        self.assertEqual(self.order2.get_total_cost, 16000)

    def test_default_address(self):
        self.assertIsNotNone(self.costumer1.default_address)
        self.assertEqual(self.costumer1.default_address.id, 1)

    def test_order(self):
        self.assertIsNotNone(self.order1.costumer)
        self.assertIsNotNone(self.order1.status)
        self.assertIsNotNone(self.order1.costumer.addresses_set.all())
        self.assertIsNotNone(self.order1.costumer.default_address)

    def test_order_items(self):
        self.assertIsNotNone(self.order1.order_items.all())
        self.assertEqual(self.item_order1.order_id, self.item_order2.order_id)
