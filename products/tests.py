from django.test import TestCase

# Create your tests here.
from products.models import Discount, Products, Categories


class TestProductDiscount(TestCase):
    def setUp(self):
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

    def test_FinalPriceProduct(self):
        self.assertEqual(self.product1.final_price(), 16000)
        self.assertEqual(self.product2.final_price(), 15000)

    def test_Categories(self):
        self.assertEqual(self.product1.category.last().type, "Mobile")
        self.assertEqual(self.product2.category.first().type, "Electronic")
