# Generated by Django 5.0.2 on 2024-08-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0004_iuser_alter_customuser_password'),
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
        migrations.RenameModel(
            old_name='IUser',
            new_name='SingUpIUser',
        ),
    ]