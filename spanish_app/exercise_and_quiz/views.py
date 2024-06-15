from django.shortcuts import render

from exercise_and_quiz.models import Exercises


# Create your views here.
def exercise_index(request):
    exercises = Exercises.objects.filter(lesson_id=1)
    context = {'title': 'Exercises page', 'exercises': exercises}
    return render(request, 'exercise_and_quiz/exercises.html', context)
