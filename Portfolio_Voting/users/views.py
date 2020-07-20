from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from users.models import User

# Create your views here.
def login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		USER_EXIST = len(User.objects.all().filter(username=username))
		print(USER_EXIST)
		if USER_EXIST == 1:
			user = auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				auth.login(request, user)
				return redirect(reverse('index'))
			else:
				messages.add_message(request, messages.ERROR, '學號或密碼錯誤')
		else:
			NEW_USER_RECORD = User.objects.create(username=username, is_active=True, is_admin=False)
			NEW_USER_RECORD.set_password(password)
			NEW_USER_RECORD.save()
			print(NEW_USER_RECORD)

			user = auth.authenticate(username=username, password=password)
			auth.login(request, user)
			return redirect(reverse('index'))

			'''
			if verify(username, password) == True:
				First, add user record to database.
				Second, login this poll website.
			else:
				SHOW messages.ERROR
			'''	

	return render(request, 'registration/login.html', locals())    


def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))


def verify(username, password):
	pass