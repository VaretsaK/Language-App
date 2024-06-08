from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def admin_index(request):
    return HttpResponse("Admin and moderation test page.")


def admin_test(request):
    return HttpResponse("<h1> Test Admin Test </h1>")
