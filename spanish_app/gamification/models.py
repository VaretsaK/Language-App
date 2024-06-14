from django.db import models


class Achievements(models.Model):
    achievement_name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    criteria = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.achievement_name}"


class UserAchievements(models.Model):
    user_id = models.ForeignKey("user_management.Users", on_delete=models.CASCADE)
    achievement_id = models.ForeignKey(Achievements, on_delete=models.CASCADE)
    achieved_at = models.DateField(auto_now=True)
