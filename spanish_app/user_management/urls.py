from django.urls import path

from .views import user_index

urlpatterns = [
    path('', user_index, name="user_index"),
]