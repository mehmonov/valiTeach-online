from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .utils import get_lessons, get_lesson
from .form import LessonForm, CourseForm

def getLessons(request, course, token):
    lessons = get_lessons( course, token)
    
    context = {
        'lessons': lessons,
        'token':token
    }
    return render(request, 'lessons/index.html', context)


def getLessonsItem(request,course, lesson, token):
  
    lesson_item = get_lesson(course, lesson, token)
    lessons = get_lessons( course, token)

    context = {
        'lesson': lesson_item,
        'lessons': lessons,
        'token':token
    }
    return render(request, 'lessons/index.html', context)


class AddLesson(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.status == 'Admin':
            form = LessonForm()
            return render(request, 'admin/addLesson.html', {'form': form})
    def post(self, request):
        if request.user.is_authenticated and request.user.status == 'Admin':
            form = LessonForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return render(request, 'admin/addLesson.html', {'form': form})

class AddCourse(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.status == 'Admin':
            form = CourseForm()
            return render(request, 'admin/addCourse.html', {'form': form})
    def post(self, request):
        if request.user.is_authenticated and request.user.status == 'Admin':
            form = CourseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return render(request, 'admin/addCourse.html', {'form': form})
