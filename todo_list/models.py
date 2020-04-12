from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class List(models.Model):
	HIGH = 'High'
	MEDIUM = 'Medium'
	LOW = 'Low'

	priority_choices = [
		(HIGH, 'High'),
		(MEDIUM, 'Medium'),
		(LOW, 'Low'),
		]

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	item = models.CharField(max_length=200)
	duedate = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
	priority = models.CharField(max_length=10, choices=priority_choices)
	completed = models.BooleanField(default=False)
	
	def __str__(self):
		return self.item