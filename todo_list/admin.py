from django.contrib import admin
from .models import List, ToDoList, Item


# Register your models here.
admin.site.register(List)
admin.site.register(ToDoList)
admin.site.register(Item)