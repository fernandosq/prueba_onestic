from collections import defaultdict
from decimal import Decimal
from django.db.models import QuerySet
from .models import OrderCount


def generate_orders_summary():
    order_query = OrderCount.objects.all().query
    order_query.group_by = ["order"]
    result = QuerySet(query=order_query,model=OrderCount)
    summary = defaultdict(Decimal)
    for order in result:
        summary[order.order.id] += order.count * order.product.cost
    return summary
