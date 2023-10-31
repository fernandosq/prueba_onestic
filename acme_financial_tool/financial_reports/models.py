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


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.DecimalField() # I use decimal because is more precise than a float

    def __str__(self):
        return f"Product ID: {self.id} - Name: {self.name} Cost: {self.cost}"
