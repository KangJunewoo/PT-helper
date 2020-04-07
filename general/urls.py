from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_process/', views.login_process, name='login_process'),
    path('main/', views.main, name='main'),
    path('guide/', views.guide, name='guide'),

]