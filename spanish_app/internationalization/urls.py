from django.urls import path

from .views import int_index

urlpatterns = [
    path('', int_index, name="int_index"),
]