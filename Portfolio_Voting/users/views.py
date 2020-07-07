from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import RegisterForm

# Create your views here.
def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(username=username, password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		print('pass', username)
		return redirect(reverse('portfolios:index'))
	else:
		print('no pass', username)
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