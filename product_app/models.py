from django.db import models
from general_app.models import CustomUser

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    price = models.FloatField(null=False)
    description = models.TextField(null=True)
    image_url = models.URLField(null=True)

    class Meta:
        db_table = 'product'

class Cart(models.Model):
    # keeping only user id & user create at cart
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart'
    

class CartItem(models.Model):
    # keeping only cart id, product id & quantity product
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return self.quantity * self.product.price
        
    class Meta:
        db_table = 'cart_item'