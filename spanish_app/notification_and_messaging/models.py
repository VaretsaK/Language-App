from django.db import models


class Notifications(models.Model):
    user_id = models.ForeignKey("user_management.Users", on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    is_read = models.BooleanField()
    created_at = models.DateField(auto_now=True)
