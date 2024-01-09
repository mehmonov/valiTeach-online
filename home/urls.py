from django.urls import path, include
from .views import Home, AddToken

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('addAdminToken', AddToken.as_view(), name='addToken'),
    
 
    

]
