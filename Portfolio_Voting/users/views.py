from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from users.models import User
from users.forms import RegisterForm

# Create your views here.
def login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)

		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect(reverse('index'))
		else:
			messages.add_message(request, messages.ERROR, '學號或密碼錯誤')
	
	return render(request, 'registration/login.html', locals())    


def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))


def register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(reverse('users:login'))
	return render(request, 'registration/register.html', {'form':form})