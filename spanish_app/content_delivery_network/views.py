from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def cdn_index(request):
    return HttpResponse("CDN test page.")
