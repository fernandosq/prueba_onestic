from django.test import TestCase
from .data_processing import deserialize_customer_csv, deserialize_products_csv

# Create your tests here.


class DataProcessingTest(TestCase):

    def test_read_customers(self):
        customers = list(deserialize_customer_csv("../customers.csv"))
        self.assertEqual(len(customers), 60)

    def test_read_products(self):
        products = list(deserialize_products_csv("../products.csv"))
        self.assertEqual(len(products), 6)


