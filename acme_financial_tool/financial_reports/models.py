from django.db import models

class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order ID: {self.id_order}, Total: {self.total} euros"
