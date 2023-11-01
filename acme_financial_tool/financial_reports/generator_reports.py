from collections import defaultdict
from decimal import Decimal
from .models import OrderCount


def generate_orders_summary():
    order_query = OrderCount.objects.all()
    summary = defaultdict(Decimal)
    for order in order_query:
        summary[order.order.id] += order.count * order.product.cost
    return summary


def generate_product_summary():
    order_query = OrderCount.objects.all()
    summary = defaultdict(set)
    for order in order_query:
        summary[order.product.id].add(order.order.customer.id)
    return {k: ",".join(str(x) for x in v) for k, v in summary.items()}

