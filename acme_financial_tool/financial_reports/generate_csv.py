import csv
from .generator_reports import generate_orders_summary, generate_product_summary, generate_ranking_customer_summary


def generate_order_prices_csv():
    with open('order_prices.csv', 'w', newline='') as csv_file:
        fieldnames = ['id', 'total']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        orders_summary = generate_orders_summary()
        for order_id, total in orders_summary.items():
            writer.writerow({'id': order_id, 'total': total})


def generate_product_customers_csv():
    with open('product_customers.csv', 'w', newline='') as csv_file:
        fieldnames = ['id', 'customer_ids']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        product_summary = generate_product_summary()
        for product_id, list_customers_ids in product_summary.items():
            writer.writerow({'id': product_id, 'customer_ids': list_customers_ids})


def generate_customer_ranking_csv():
    with open('customer_ranking.csv', 'w', newline='') as csv_file:
        fieldnames = ['id', 'name', "lastname", "total"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        ranking_customer_summary = generate_ranking_customer_summary()
        for customer, total in ranking_customer_summary.items():
            writer.writerow({'id': customer.id, "name": customer.firstname, "lastname": customer.lastname, 'total': total})
