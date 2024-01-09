from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.shortcuts import redirect

from .form import CustomUserCreationForm, UserForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model

User = get_user_model()

class Login(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'users/login.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Foydalanuvchi ro'yxatdan o'tmagan yoki parol noto'g'ri")
            return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    
    return render(request, 'users/login.html')



class AddUser(FormView):
    template_name = 'admin/addUser.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class MyProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/myProfile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user
