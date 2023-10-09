from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('users/',views.usersTable,name='usersTable'),
    path('usersForm/',views.usersForm,name='usersForm'),
]