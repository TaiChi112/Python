from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password,check_password

class CustomUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    def hash_password(self, password):
        self.password = make_password(password)
    
    def check_password(self,password):
        return check_password(password, self.password)

# class SignUpIUser(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True,max_length=100)
#     password = models.CharField(max_length=100)

# class SignInIUser(models.Model):
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)

# class Account(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

#     def hash_password(self, password):
#         self.password = make_password(password)
    
#     def check_password(self,password):
#         return check_password(password, self.password)
    
# class CustomUser(models.Model):
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)

#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

#     @classmethod
#     def create_user(cls, email, username, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')

#         user = cls(
#             email=email,
#             username=username,
#         )
#         user.set_password(password)
#         user.save(using=models.DEFAULT_DB_ALIAS)
#         return user

#     @classmethod
#     def create_superuser(cls, email, username, password=None):
#         user = cls.create_user(
#             email=email,
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=models.DEFAULT_DB_ALIAS)
#         return user
