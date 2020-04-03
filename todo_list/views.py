from django.shortcuts import render, redirect
from .models import List, ToDoList, Item
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings

def home(request): 
	if not request.user.is_authenticated:
		return redirect('login')

	else: 
		if request.method == 'POST': 
			form = ListForm(request.POST or None)
			
			if form.is_valid():
				fs=form.save(commit=False)
				fs.user=request.user
				fs.save()
				context={'form':form, 'all_items':List.objects.all}
				messages.success(request, ('Item has been successfully added to the list!'))
				return render(request, 'todo_list/home.html', context)
		
		else:
			all_items = List.objects.all 
			return render(request, 'todo_list/home.html', {'all_items': all_items})

def tdlist(request):
	todo_listing = []

	if not request.user.is_authenticated:
		return redirect('login')
	else: 
		for todo_list in Item.objects.all():
			todo_dict = {}
			todo_dict['list_object'] = todo_list
			todo_listing.append(todo_dict)
	return render(request, 'todo_list/todolist.html', { 'todo_listing': todo_listing })

def status_report(request): 
	todo_listing = []  

	if not request.user.is_authenticated:
		return redirect('login')
	else:
		for todo_list in ToDoList.objects.all():  
			todo_dict = {}  
			todo_dict['list_object'] = todo_list  
			todo_dict['item_count'] = todo_list.item_set.count()  
			todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()  
			todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)  
			todo_listing.append(todo_dict)  
		return render(request, 'todo_list/statusreport.html', { 'todo_listing': todo_listing })

def about(request):
	context = {'first_name': 'John', 'last_name': 'Tyler'}
	return render(request, 'todo_list/about.html', context)

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item has been deleted from the list!'))
	return redirect('home')

def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home') 

def uncross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home') 

def edit(request, list_id):
	if request.method == 'POST': 
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, ('Item has edited!'))
			return redirect('home')

	else:
		item = List.objects.get(pk=list_id)
		return render(request, 'todo_list/edit.html', {'item': item})