
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
from django.utils import timezone

timezone.activate("Asia/Kolkata")


class items(models.Model):
    tax = {'Medicine': 5, 'Food': 5, 'Music': 3, 'Total': 5, 'Imported': 18}

    choices = (("Medicine", "Medicine"),
               ("Food", "Food"),
               ("Music", "Music"),
               ("Imported", "Imported"),
               ("Book", "Book"))

 
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    purchased_date = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=30)
    item_category = models.CharField(max_length=10,choices=choices)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        ordering = ['item']
