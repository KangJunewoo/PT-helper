from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('uploads/', views.uploads, name='uploads'),
    path('search/', views.search, name='search'),
    path('show/', views.show, name='show'),
    path('presentaionDetail/', views.mypage, name='mypage'),
    path('editPresentaion/', views.editPresentaion, name='editPresentaion'),
    path('deletePresentation', views.deletePresentation, name='deletePresentation'),
]