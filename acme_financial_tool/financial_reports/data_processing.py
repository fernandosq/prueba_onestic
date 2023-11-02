import csv
from .models import Customer, Product, Order, OrderCount


def deserialize_customer_csv(csv_file):
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        id = int(row['id'])
        first_name = row['firstname']
        last_name = row['lastname']
        customer = Customer(id, first_name, last_name)
        yield customer


def deserialize_products_csv(csv_file):
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        id = int(row['id'])
        name = row['name']
        cost = round(float(row['cost']), 2)
        product = Product(id, name, cost)
        yield product


def deserialize_orders_csv(csv_file):
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        id = int(row['id'])
        customer = row['customer']
        products = row['products'].split()
        order = Order(id)
        order.customer = Customer.objects.get(pk=customer)
        products_ids = [int(product) for product in products]
        yield order, products_ids


def save_csv_data(customer_csv, product_csv, orders_csv):
    for customer in deserialize_customer_csv(customer_csv):
        customer.save()
    for product in deserialize_products_csv(product_csv):
        product.save()
    orders = list(deserialize_orders_csv(orders_csv))
    for order, products in orders:
        order.save()
        for product_id in products:
            OrderCount.add_product(order.id, product_id)
