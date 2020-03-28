from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'), 
    path('logout/', views.logout_user, name='logout'),
    path('userprofile/', views.profile_user, name='profile'),
    path('register/', views.register_user, name='register'), 
]