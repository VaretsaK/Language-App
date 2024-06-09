from django.urls import path

from .views import cdn_index

urlpatterns = [
    path('', cdn_index, name="cdn_index"),
]