from django.urls import path
from . import views

urlpatterns=[
    # 메인화면, 로그인 세션 유무로 페이지 결정
    path('', views.home, name='home'),
    path('uploads/', views.uploads, name='uploads'),
    path('search/', views.search, name='search'),
    path('show/', views.show, name='show'),
    path('presentaionDetail/', views.mypage, name='mypage'),
    path('editPresentaion/', views.editPresentaion, name='editPresentaion'),
    path('deletePresentation', views.deletePresentation, name='deletePresentation'),
]