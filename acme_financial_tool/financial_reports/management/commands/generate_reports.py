import argparse
from django.core.management.base import BaseCommand
from financial_reports.data_processing import save_csv_data
from financial_reports.generate_csv import generate_order_prices_csv, generate_customer_ranking_csv, \
    generate_product_customers_csv


class Command(BaseCommand):
    help = 'Generates CSV reports from input CSV files'

    def add_arguments(self, parser):
        parser.add_argument('customers_file')
        parser.add_argument('products_file')
        parser.add_argument('orders_file')

    def handle(self, *args, **options):
        customers_file = options['customers_file']
        products_file = options['products_file']
        orders_file = options['orders_file']

        with open(customers_file, 'r', newline='') as customers_csv_file, \
             open(products_file, 'r', newline='') as products_csv_file, \
             open(orders_file, 'r', newline='') as orders_csv_file:
            save_csv_data(customers_csv_file, products_csv_file, orders_csv_file)

        with open("order_prices.csv", 'w', newline='') as order_prices_report, \
             open("product_customers.csv", 'w', newline='') as product_customers_report, \
             open("customer_ranking.csv", 'w', newline='') as customer_ranking_report:
            generate_order_prices_csv(order_prices_report)
            generate_product_customers_csv(product_customers_report)
            generate_customer_ranking_csv(customer_ranking_report)

            self.stdout.write(self.style.SUCCESS('CSV files generated successfully'))
