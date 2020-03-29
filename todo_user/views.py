from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm

def home(request):
    return render(request, 'todo_user/home.html',{})

def login_user(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request,('You have successfully logged in!'))
            return redirect('home') 
        else: 
            messages.success(request, ('Error logging in please try again!'))
            return redirect('login')
    else: 
        return render(request, 'todo_user/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('home')

def profile_user(request):
    return render(request, 'todo_user/profile.html', {})

def profile_edit(request):
    if request.method == 'POST': 
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid(): 
            form.save()
            messages.success(request, ('You have updated your profile!'))
            return redirect('profile')
    else: 
        form = EditProfileForm(instance=request.user)
        
    context = {'form': form}
    return render(request, 'todo_user/editprofile.html', context)

def change_password(request): 
    if request.method == 'POST': 
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid(): 
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have changed your password!'))
            return redirect('profile')
    else: 
        form = PasswordChangeForm(user=request.user)
        
    context = {'form': form}
    return render(request, 'todo_user/changepassword.html', context)

def register_user(request): 
    if request.method == 'POST': 
        form = SignUpForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered!'))
            return redirect('home')
    else: 
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'todo_user/register.html', context)


