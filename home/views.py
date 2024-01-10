from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from lessons.utils import get_course
from users.models import User
from lessons.models import Course, Lesson

from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .form import TokenForm
from .models import Tokens
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home/index.html"

    def dispatch(self, request, *args, **kwargs):
        user_count = User.objects.count()
        course_count = Course.objects.count()
        lesson_count = Lesson.objects.count()
        if request.user.status == 'Admin':
            context = {
                'user_count': user_count,
                'course_count': course_count,
                'lesson_count': lesson_count
            }
            return render(request, 'admin/index.html', context)  
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        user_courses = get_course(self.request.user)
        context = super().get_context_data(**kwargs)
        context['kurs'] = user_courses  
        return context



class AddToken(FormView):
    template_name = 'admin/addToken.html'
    form_class = TokenForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def blank(request):
    return render(request, '404.html')
def info(request):
    return render(request, 'info.html')
