from django.db import models

# Create your models here.


class Languages(models.Model):
    language_name = models.CharField(max_length=128)
    language_code = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.language_name}"


class Lessons(models.Model):
    lesson_name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.lesson_name}"
