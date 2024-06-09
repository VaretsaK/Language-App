from django.db import models
from user_management.models import Users

# Create your models here.


class Achievements(models.Model):
    achievement_name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    criteria = models.CharField(max_length=254)


class UserAchievements(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    achievement_id = models.ForeignKey(Achievements, on_delete=models.CASCADE)
    achieved_at = models.DateField(auto_now=True)
