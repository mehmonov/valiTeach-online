from django.urls import path, include
from .views import Home, AddToken, blank, info

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('addAdminToken', AddToken.as_view(), name='addToken'),
    path('blank/', blank, name='blank'),
    path('info/', info, name='info'),
    
]
