from django.urls import path

from .views import progr_index

urlpatterns = [
    path('', progr_index, name="progr_index"),
]