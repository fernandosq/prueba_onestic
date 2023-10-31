from django.db import models

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return f"ID: {self.id}, customer: {self.customer}, products: {self.products}"


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)

    def __str__(self):
        return f"Customer ID: {self.id} - Name: {self.firstname} Lastname : {self.lastname}"
