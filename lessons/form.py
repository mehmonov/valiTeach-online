from django import forms
from .models import Lesson, Course

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'course', 'link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'price', 'teacher', 'coupon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher': forms.TextInput(attrs={'class': 'form-control'}),
            'coupon': forms.TextInput(attrs={'class': 'form-control'}),
        }
