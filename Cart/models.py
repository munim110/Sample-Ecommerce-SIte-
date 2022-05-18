from pyexpat import model
from django.db import models
from Product.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    def get_total_price(self):
        total_price = 0
        for p in self.product.all():
            total_price += p.price
        return total_price