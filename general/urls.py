from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    # path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('login_process/', views.login_process, name='login_process')
    # path('logout/', views.logout, name='logout'),
    # path('mypage/', views.mypage, name='mypage'),
    # path('editProfile/', views.editProfile, name='editProfile'),
    # path('changePassword', views.chagnePassword, name='changePassword'),
]