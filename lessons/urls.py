from django.urls import path

from . import views

urlpatterns = [
    path('lessons/<str:course>/<str:token>/', views.getLessons, name='get_lessons'),
    path('lesson/<str:course>/<str:lesson>/<str:token>/', views.getLessonsItem, name='get_lessons_item'),
    path('adminAddLesson/', views.AddLesson.as_view(), name='addLesson'),
    path('adminAddCourse/', views.AddCourse.as_view(), name='addCourse')
]
