from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    #여기부터 url 입력 ㄱㄱ
]