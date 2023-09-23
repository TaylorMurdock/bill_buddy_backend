from django.db import models

# Create your models here.


class Bills(models.Model):
    name_of_subscription = models.CharField(max_length=100)
    # find a way todo url links.... image db with all sub pictures in that db for the user to select from....... have it so when the sub name matches image name in db auto does it
    # lets wait for imgs
    subscription_image_url = models.CharField(max_length=400)
    bill_date = models.CharField(max_length=100)
    subscription_price = models.CharField(max_length=100)
