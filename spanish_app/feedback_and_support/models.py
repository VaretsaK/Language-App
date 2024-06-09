from django.db import models
from user_management.models import Users

# Create your models here.


class Feedback(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    rating = models.IntegerField()
    created_at = models.DateField(auto_now=True)
