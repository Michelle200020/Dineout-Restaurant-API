
from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cuisines = models.JSONField()  # Assuming you're using Django 3.1 or later
    price = models.IntegerField()
    location = models.CharField(max_length=100)
    open_from = models.CharField(max_length=8)  # Adjust max_length according to your data
    open_till = models.CharField(max_length=8)  # Adjust max_length according to your data
    offer = models.CharField(max_length=20)
    offer_type = models.CharField(max_length=20)
    restaurant_type = models.CharField(max_length=100)
    features = models.JSONField()  # Assuming you're using Django 3.1 or later
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    votes = models.CharField(max_length=20)
    reviews = models.CharField(max_length=20)
    outlet_count = models.IntegerField()

    def __str__(self):
        return self.name

