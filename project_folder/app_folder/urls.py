from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.vishnu,name='vishnu'),
    path('login_page',views.login_page,name='login_page'),
    path('login_page1',views.login_page1,name='login_page1'),
    
]
