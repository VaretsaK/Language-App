from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=128)  # TODO: has to be hashed
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    profile_picture = models.ImageField(upload_to="user_management/profile_pictures")
    preferred_language = models.CharField(max_length=16, default="english")
    subscription_status = models.CharField(max_length=16, default="free")
