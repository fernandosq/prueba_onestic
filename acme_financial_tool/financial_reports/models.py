from django.db import models

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return f"ID: {self.id}, id customer: {self.customer.id}, products: {self.product}"

