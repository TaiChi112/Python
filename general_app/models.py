# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):# checking email and username is sending?
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)# hash password 
        user.save(using=self._db)# save user in DB
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' #auth instance username
    REQUIRED_FIELDS = ['username'] # strict

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):#check permission access anything in app
        return True

    def has_module_perms(self, app_label):# check permission access module
        return True

    @property
    def is_staff(self):# checking user is admin
        return self.is_admin

    class Meta:
        db_table = 'custom_user'