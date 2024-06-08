from django.urls import path

from .views import admin_index, admin_test

urlpatterns = [
    path('', admin_index, name="admin_index"),
    path('admin_test/', admin_test, name="admin_test"),
]
