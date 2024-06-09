from django.urls import path

from .views import analytics_index

urlpatterns = [
    path('', analytics_index, name="analytics_index"),
]