from django.contrib import admin
from django.urls import path, include, re_path
from todo_list import views
from django.conf.urls import url

urlpatterns = [
 #  path('admin/', admin.site.urls),
 #  path('', include('todo_list.urls')),
    re_path(r'^todo_list/$', views.todo_list),
    re_path(r'^todo_list/([0-9]+)$', views.todo_detail),
 #  path('user/', include('todo_user.urls')),
]

