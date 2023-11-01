from django.test import TestCase
from .data_processing import deserialize_customer_csv, deserialize_products_csv, deserialize_orders_csv
from .models import Customer, Product


# Create your tests here.


class Products:
    pass


class DataProcessingTest(TestCase):

    def test_read_customers(self):
        customers = list(deserialize_customer_csv("../customers.csv"))
        self.assertEqual(len(customers), 60)

    def test_read_products(self):
        products = list(deserialize_products_csv("../products.csv"))
        self.assertEqual(len(products), 6)

    def test_read_orders(self):
        for customer in deserialize_customer_csv("../customers.csv"):
            customer.save()
        self.assertEqual(Customer.objects.all().count(),60)
        for product in deserialize_products_csv("../products.csv"):
            product.save()
        self.assertEqual(Product.objects.all().count(), 6)
        orders = list(deserialize_orders_csv("../orders.csv"))
        self.assertEqual(len(orders), 50)

        for order, products in orders:
            order.save()
            order.products.add(*products)
            order.save()
            self.assertEqual(len(set(products)), order.products.all().count())



