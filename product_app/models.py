from django.db import models
from general_app.models import CustomUser

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    description = models.TextField(null=True)
    image_url = models.URLField(null=True)

    class Meta:
        db_table = 'product'

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart'
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.product.price
    
    # def get_total_price_pices(self):
    #     return self.quantity
    class Meta:
        db_table = 'cart_item'