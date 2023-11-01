from django.db import models


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through="OrderCount")

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
    cost = models.DecimalField(max_digits=10, decimal_places=2) # I use decimal because is more precise than a float

    def __str__(self):
        return f"Product ID: {self.id} - Name: {self.name} Cost: {self.cost}"


class OrderCount(models.Model):
    order = models.ForeignKey('Order', to_field='id', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', to_field='id', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    def __str__(self):
        return f" Customer ID: {self.customer_id.id}"

    @classmethod
    def add_product(cls, order_id, product_id):
        from django.db.models import F
        return cls.objects.update_or_create(order_id=order_id,
                                     product_id=product_id,
                                     defaults={"count": F("count") + 1},
                                     create_defaults={"count": 0})

