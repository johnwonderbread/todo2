from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'), 
    path('logout/', views.logout_user, name='logout'),
    path('userprofile/', views.profile_user, name='profile'),
    path('register/', views.register_user, name='register'), 
    path('editprofile/', views.profile_edit, name='profile_edit'),
    path('changepassword/', views.change_password, name='change_password')
]