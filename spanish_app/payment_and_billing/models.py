from django.db import models
from user_management.models import Users

# Create your models here.


class Subscriptions(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
