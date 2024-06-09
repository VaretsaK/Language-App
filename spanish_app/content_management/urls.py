from django.urls import path

from .views import content_index

urlpatterns = [
    path('', content_index, name="content_index"),
]