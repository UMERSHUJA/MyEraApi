from django.db import models
from datetime import datetime



class Startup(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Startup')
    prices = models.CharField(max_length=200)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    is_sponsered = models.BooleanField(default=True, blank=True)
    submission_date = models.DateTimeField(default=datetime.now, blank=False)
    published = models.BooleanField(default=False)
    user_id = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.product_name




