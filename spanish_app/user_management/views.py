from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def user_index(request):
    return HttpResponse("Users test page.")
