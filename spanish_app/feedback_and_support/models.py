from django.db import models


class Feedback(models.Model):
    user_id = models.ForeignKey("user_management.Users", on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    rating = models.IntegerField()
    created_at = models.DateField(auto_now=True)
