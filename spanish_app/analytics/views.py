from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def analytics_index(request):
    return HttpResponse("Analytics test page.")
