from django.urls import path

from .views import exercise_index

urlpatterns = [
    path('', exercise_index, name="exercise_index"),
]