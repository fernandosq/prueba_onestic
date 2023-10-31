import csv
from .models import Customer,Product


def deserialize_customer_csv(csv_file_path):

    with open(csv_file_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            id = int(row['id'])
            first_name = row['firstname']
            last_name = row['lastname']
            customer = Customer(id, first_name, last_name)
            yield customer


def deserialize_products_csv(csv_file_path):

    with open(csv_file_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            id = int(row['id'])
            name = row['name']
            cost = round(float(row['cost']), 2)
            product = Product(id, name, cost)
            yield product

