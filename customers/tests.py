from django.test import TestCase

# Create your tests here.
from customers.models import Costumers


class TestCustomer(TestCase):
    def setUp(self):
        self.costumer1 = Costumers.objects.create(username="phoenix", password="1234", f_name="mobin", l_name="atashi",
                                                  phone="626426246", email="mobinatashi2@gmail.com")

    def test1(self):
        self.assertEqual(self.costumer1.is_active, True)
        self.assertEqual(self.costumer1.is_deleted, False)
