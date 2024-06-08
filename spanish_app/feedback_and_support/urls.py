from django.urls import path

from .views import feedback_index

urlpatterns = [
    path('', feedback_index, name="feedback_index"),
]