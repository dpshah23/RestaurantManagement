from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='index'),
    path('signup',register,name='register'),
    path('login',login,name='login'),
]
