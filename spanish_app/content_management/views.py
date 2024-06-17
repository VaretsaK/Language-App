from django.shortcuts import render

from content_management.models import Lessons


def content_index(request):
    lessons = Lessons.objects.all()
    context = {'title': 'Lessons page', 'lessons': lessons}
    return render(request, 'content_management/lessons.html', context)

