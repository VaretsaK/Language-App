from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def progr_index(request):
    return HttpResponse("Progress test page.")
