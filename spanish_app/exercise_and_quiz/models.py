from django.db import models


class Exercises(models.Model):
    lesson_id = models.ForeignKey("content_management.Lessons", on_delete=models.CASCADE)
    exercise_type = models.CharField(max_length=64)
    question_text = models.TextField(null=True, blank=True)
    correct_answer = models.CharField(max_length=64)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class UserAnswers(models.Model):
    user_id = models.ForeignKey("user_management.Users", on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=64)
    is_correct = models.BooleanField()
    answered_at = models.DateField(auto_now=True)
