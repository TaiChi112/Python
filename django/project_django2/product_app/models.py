from django.db import models

# Create your models here.

class Product(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3,null=True)
    image_url = models.URLField(null=True)