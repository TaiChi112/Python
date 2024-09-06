from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    description = models.TextField(null=True)
    image_url = models.URLField(null=True)

    class Meta:
        db_table = 'product'