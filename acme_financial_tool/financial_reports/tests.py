from decimal import Decimal
from django.test import TestCase
from .data_processing import deserialize_customer_csv, deserialize_products_csv, deserialize_orders_csv
from .models import Customer, Product, OrderCount, Order
from .generator_reports import generate_orders_summary, generate_product_summary, generate_ranking_customer_summary


class DataProcessingTest(TestCase):

    def setUp(self):
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
            for product_id in products:
                OrderCount.add_product(order.id, product_id)
            self.assertEqual(len(set(products)), order.products.all().count())

    def test_read_customers(self):
        customers = list(deserialize_customer_csv("../customers.csv"))
        self.assertEqual(len(customers), 60)

    def test_read_products(self):
        products = list(deserialize_products_csv("../products.csv"))
        self.assertEqual(len(products), 6)

    def test_orders_summary(self):
        summary = generate_orders_summary()
        self.assertEqual(len(summary), 50)
        self.assertEqual(summary[0], Decimal("18.94"))

    def test_product_summary(self):
        summary = generate_product_summary()
        self.assertEqual(len(summary), 6)

    def test_ranking_customer_summary(self):
        summary = generate_ranking_customer_summary()
        self.assertEqual(len(summary), 36)




