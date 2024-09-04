from django.db import models

class Subscription(models.Model):

    STATUS = [
        ('unapproved','Unapproved'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    ]
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=15,choices=STATUS,default='unapproved')
    registered_at = models.DateTimeField(auto_now_add=True)