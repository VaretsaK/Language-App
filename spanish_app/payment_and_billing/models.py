from django.db import models


class Subscriptions(models.Model):
    user_id = models.ForeignKey("user_management.Users", on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.subscription_type}"
