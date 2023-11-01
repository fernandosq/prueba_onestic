from collections import defaultdict
from decimal import Decimal
from .models import OrderCount


def generate_orders_summary():
    order_query = OrderCount.objects.all()
    summary = defaultdict(Decimal)
    for order in order_query:
        summary[order.order.id] += order.count * order.product.cost
    return summary
