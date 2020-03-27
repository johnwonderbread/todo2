from django.shortcuts import render

def login(request):
    return render(request, 'user/login.html',{})

def test(request):
    return render(request, 'user/test.html',{})
    