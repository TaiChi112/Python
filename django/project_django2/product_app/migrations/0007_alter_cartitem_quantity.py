# Generated by Django 5.0.2 on 2024-09-01 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0006_remove_orderitem_order_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
