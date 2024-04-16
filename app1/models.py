from django.db import models

# Create your models here.

class customerPurchaseInfo(models.Model):
    customer_ref = models.IntegerField()
    name = models.TextField()
    address = models.TextField()
    email = models.EmailField()
    date = models.DateField()
    membership = models.IntegerField()