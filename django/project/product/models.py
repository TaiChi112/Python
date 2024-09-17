from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60, null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    # is_premium = models.BooleanField(default=False)
    # promotion_end_at = models.DateTimeField(null=True)

# class Product(models.Model):
#     title = models.CharField(max_length=60)
#     price = models.IntegerField()
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)