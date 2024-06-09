from django.db import models
from user_management.models import Users
from content_management.models import Lessons

# Create your models here.


class UserProgress(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    lesson_id = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)
    score = models.IntegerField()
    last_accessed = models.DateField(auto_now=True)
