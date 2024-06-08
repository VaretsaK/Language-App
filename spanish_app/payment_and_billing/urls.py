from django.urls import path

from .views import pay_index

urlpatterns = [
    path('', pay_index, name="pay_index"),
]