from django.shortcuts import render

from user_management.models import Users
from content_management.models import Lessons


def user_index(request):
    lessons = Lessons.objects.all()
    user = Users.objects.get(pk=1)
    context = {'user': user, 'title': 'Home page', 'lessons': lessons}
    return render(request, 'user_management/home_page.html', context)
