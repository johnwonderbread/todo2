from django.shortcuts import render, redirect
from .models import List
from .serializers import *
from .forms import ListForm

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        data = List.objects.all()

        serializer = ListSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def todo_detail(request, id):
    try:
        list = List.objects.get(id=id)
    except List.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ListSerializer(list, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
				context={'form':form, 'all_items':List.objects.all()}
				messages.success(request, ('Item has been successfully added to the list!'))
				return render(request, 'todo_list/home.html', context)
		
		else:
			form = ListForm()
			all_items = List.objects.all()
			context = {'form':form, 'all_items':all_items}
			return render(request, 'todo_list/home.html', context)

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