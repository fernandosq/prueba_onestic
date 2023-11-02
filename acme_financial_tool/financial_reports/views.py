from django.http import JsonResponse
from django.shortcuts import render
from io import StringIO, BytesIO

from django.views.decorators.csrf import csrf_exempt

from .data_processing import save_csv_data
# Create your views here.

@csrf_exempt
def api_upload_files(request):
    if request.method == 'POST':
        all_files = request.FILES
        customer_csv = all_files["customers.csv"]
        product_csv = all_files["products.csv"]
        orders_csv = all_files["orders.csv"]
        customer_csv = StringIO(customer_csv.read().decode("utf-8"))
        product_csv = StringIO(product_csv.read().decode("utf-8"))
        orders_csv = StringIO(orders_csv.read().decode("utf-8"))
        save_csv_data(customer_csv, product_csv, orders_csv)

        return JsonResponse({'message': 'CSV file processed successfully'})
    else:
        return JsonResponse({'error': 'Disallowed method'}, status=405)

