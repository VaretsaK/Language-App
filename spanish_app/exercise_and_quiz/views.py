from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def exercise_index(request):
    return HttpResponse("Exercise test page.")
