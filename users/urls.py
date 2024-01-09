from django.urls import path, include
from .views import Login, logout_user, AddUser, MyProfile

urlpatterns = [
    path('login/',Login.as_view(), name='login' ),
    path('logout/',logout_user, name='logout' ),
    path('addAdminUser/', AddUser.as_view(), name='adminAddUser'),
    path('my_profil/', MyProfile.as_view(), name='my_profil'),
    
    
]
