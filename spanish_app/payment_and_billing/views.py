from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def pay_index(request):
    return HttpResponse("Payment test page.")
