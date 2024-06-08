from django.urls import path

from .views import notif_index

urlpatterns = [
    path('', notif_index, name="notif_index"),
]