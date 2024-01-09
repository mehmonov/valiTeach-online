from .models import Course
from users.models import User
from home.models import Tokens
from lessons.models import Lesson, Course
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import HttpResponse

import secrets

def get_course(username):
    """ 
        Username kiriting. Sizga shu userga tegishli tokenni qaytaradi. 

    """
    try:
        user = User.objects.get(username=username)
        tokens = Tokens.objects.filter(user=user, expiration_time__gt=timezone.now().date()).all()
        
        if not tokens:
            return "Token mavjud emas yoki muddati o'tib ketgan"
        
        courses = [token.course for token in tokens]

        return courses
    except ObjectDoesNotExist:
        return "User mavjud emas"



def get_lessons(course_id, token):
    
    """
        Kursning haqiqiy token bilan murojaat qilinayotganini tekshiradi. 
    """
    try:
        # Tokenni topish
        token_obj = Tokens.objects.get(token=token)
        # Tokenning muddati o'tmaganligini tekshirish
        if token_obj.expiration_time < timezone.now().date():
            raise PermissionDenied("Tokenning muddati o'tgan")

        # Kursni topish
        course = Course.objects.get(pk=course_id)

        # Tokenning kursga tegishli ekanligini tekshirish
        if token_obj.course.pk != course.pk:
            raise PermissionDenied("Token bu kurs uchun emas")

        # Kursga oid hamma darslarni qaytarish
        lessons = Lesson.objects.filter(course=course)
        return lessons

    except Tokens.DoesNotExist:
        return HttpResponse("Token topilmadi")
    except PermissionDenied as e:
        return HttpResponse(str(e))
    except Course.DoesNotExist:
        return HttpResponse("Kurs topilmadi")



def get_lesson(course, lesson, token):
    """
        Har bir darsni qaytaradi raqami bilan birga. Darsni videosi shu yerdan keladi
    """
    try:
        # Tokenni topish
        token_obj = Tokens.objects.get(token=token)
        
        # Tokenning muddati o'tmaganligini tekshirish
        if token_obj.expiration_time < timezone.now().date():
            raise PermissionDenied("Tokenning muddati o'tgan")

        # Kursni topish
        course_obj = Course.objects.get(pk=course)

        # Tokenning kursga tegishli ekanligini tekshirish
        if token_obj.course.pk != course_obj.pk:
            raise PermissionDenied("Token bu kurs uchun emas")

        # Kursga oid hamma darslarni qaytarish
        lessons = Lesson.objects.filter(course=course_obj)

        # Berilgan darsni topish
        lesson_obj = lessons.get(pk=lesson)

        return lesson_obj

    except Tokens.DoesNotExist:
        return HttpResponse("Token topilmadi")
    except PermissionDenied as e:
        return HttpResponse(str(e))
    except Course.DoesNotExist:
        return HttpResponse("Kurs topilmadi")
    except Lesson.DoesNotExist:
        return HttpResponse("Dars topilmadi")

