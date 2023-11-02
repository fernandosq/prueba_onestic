import zipfile
from django.http import JsonResponse, HttpResponse
from io import StringIO, BytesIO
from django.views.decorators.csrf import csrf_exempt
from .data_processing import save_csv_data
from .generate_csv import generate_order_prices_csv, generate_product_customers_csv, generate_customer_ranking_csv


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
        buffer1 = StringIO()
        generate_order_prices_csv(buffer1)
        buffer2 = StringIO()
        generate_product_customers_csv(buffer2)
        buffer3 = StringIO()
        generate_customer_ranking_csv(buffer3)

        # Create a ZIP file to contain the CSV files
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zipf:
            zipf.writestr('order_prices.csv', buffer1.getvalue())
            zipf.writestr("product_customers.csv", buffer2.getvalue())
            zipf.writestr('customer_ranking.csv', buffer3.getvalue())

        # Reset CSV file buffers
        buffer1.seek(0)
        buffer2.seek(0)
        buffer3.seek(0)

        response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=archivos_csv.zip'

        # Clear buffers of CSV files and ZIP file
        buffer1.close()
        buffer2.close()
        buffer3.close()
        zip_buffer.close()

        return response
    else:
        return JsonResponse({'error': 'Disallowed method'}, status=405)

