import zipfile
from django.http import JsonResponse, HttpResponse
from io import StringIO, BytesIO
from django.views.decorators.csrf import csrf_exempt
from .data_processing import save_csv_data
from .generate_csv import generate_order_prices_csv, generate_product_customers_csv, generate_customer_ranking_csv, \
    generate_buffered_reports, zip_reports


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


@csrf_exempt
def api_download_files(request):
    if request.method == 'GET':
        buffer_order_prices_csv, buffer_product_customers_csv, buffer_customer_ranking_csv = generate_buffered_reports()

        # Create a ZIP file to contain the CSV files
        zip_buffer = zip_reports(buffer_order_prices_csv, buffer_product_customers_csv, buffer_customer_ranking_csv)
        response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=archivos_csv.zip'

        return response
    else:
        return JsonResponse({'error': 'Disallowed method'}, status=405)

