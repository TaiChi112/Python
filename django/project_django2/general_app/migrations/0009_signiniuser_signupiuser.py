# Generated by Django 5.0.2 on 2024-08-31 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0008_delete_signiniuser_delete_signupiuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignInIUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SignUpIUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
