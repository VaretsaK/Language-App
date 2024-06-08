from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def search_index(request):
    return HttpResponse("Search test page.")
