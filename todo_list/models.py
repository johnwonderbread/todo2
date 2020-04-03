from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class List(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	
	def __str__(self):
		return self.item + ' ' + str(self.completed)

PRIORITY_CHOICES = ( 
  (1, 'Low'), 
  (2, 'Normal'), 
  (3, 'High'), 
) 

class ToDoList(models.Model): 
  title = models.CharField(max_length=250, unique=True) 
  def __str__(self): 
    return self.title 
  class Meta: 
    ordering = ['title'] 

class Item(models.Model): 
  todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE) 
  task = models.CharField(max_length=250) 
  created_date = models.DateTimeField(default=datetime.datetime.now) 
  priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
  completed = models.BooleanField(default=False) 
  list_title = models.TextField(ToDoList.title)
  def __str__(self): 
    return self.title 
  class Meta: 
    ordering = ['-priority', 'task'] 