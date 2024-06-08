from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def int_index(request):
    return HttpResponse("Internationalization test page.")
