from django.db import models


class UserProgress(models.Model):
    user_id = models.ForeignKey("user_management.Users", on_delete=models.CASCADE)
    lesson_id = models.ForeignKey("content_management.Lessons", on_delete=models.CASCADE)
    status = models.CharField(max_length=64)
    score = models.IntegerField()
    last_accessed = models.DateField(auto_now=True)
