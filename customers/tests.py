from django.test import TestCase

# Create your tests here.
from core.models import User
from customers.models import Costumers


class TestCostumer(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(phone="09142520208", password="admin", email="mobinatashi2@gmail.com")
        self.costumer1 = Costumers.objects.create(user=self.user1)

    def test_user(self):
        self.assertEqual(self.costumer1.user.username, self.costumer1.user.phone)
        self.assertIn(self.costumer1.user.id, [1, 2, 3])
        self.assertEqual(self.costumer1.user.id, 1)
        self.assertEqual(self.costumer1.user.phone, "09142520208")
        self.assertEqual(self.costumer1.user.email, "mobinatashi2@gmail.com")
        self.assertNotEqual(self.costumer1.user.password, "admin")

    def test_costumer(self):
        self.assertIsNotNone(self.costumer1.id)
        self.assertIsNone(self.costumer1.default_address)
