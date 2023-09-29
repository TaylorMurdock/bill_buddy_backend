from django.db import models

# Create your models here.


class Bills(models.Model):
    name_of_subscription = models.CharField(max_length=100)
    subscription_image_url = models.CharField(max_length=400)
    bill_date = models.DateField()
    # bill_date = models.CharField(max_length=100)
    subscription_price = models.CharField(max_length=100)
