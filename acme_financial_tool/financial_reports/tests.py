from django.test import TestCase
from .data_processing import processing_customer_csv

# Create your tests here.


class DataProcessingTest(TestCase):

    def test_read_customers(self):
        customers = list(processing_customer_csv("../customers.csv"))
        self.assertEqual(len(customers), 60)

