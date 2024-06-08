from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def notif_index(request):
    return HttpResponse("Notification_and_messaging test page.")
