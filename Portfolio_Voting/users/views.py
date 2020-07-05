from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
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

def login000(request):
	USER_STUD_ID = request.POST.user.studID
	print('---', USER_STUD_ID)
	# request.session['USER_INPUT_STUD_ID'] = USER_STUD_ID
	# print(request.session['USER_INPUT_STUD_ID'])

	### Test for session ###
	print(username)
	request.session['studID'] = username
	studID = request.session['studID']
	print(studID, "request.session['studID']")
    

def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))

def register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(reverse('users:login'))
	context = {
		'form': form
	}
	return render(request, 'registration/register.html', {'form':form})
	
def get_user_info(request):
	if 'user_input_fullname' in request.POST and 'user_input_department' in request.POST:
		USER_FULLNAME = request.POST.get('user_input_fullname')
		USER_DEPARTMENT = request.POST.get('user_input_department')
		USER_ISACTIVE = request.POST.get('user_input_isactive')
		USER_ISADMIN = request.POST.get('user_input_isadmin')
		
		print(USER_FULLNAME, USER_DEPARTMENT, USER_ISACTIVE, USER_ISADMIN)

		request.session['USER_INPUT_FULLNAME'] = USER_FULLNAME
		request.session['USER_INPUT_DEPARTMENT'] = USER_DEPARTMENT

		## 存到 User 資料表 ## ------------------------------
		one_user_info = User.objects.create(
			studID=username,
			fullName=USER_FULLNAME, 
			department=USER_DEPARTMENT, 
			is_active=USER_ISACTIVE,
			is_admin=USER_ISADMIN,
		)
		User.save()
		'''
		### TESTING: 傳遞 session ###
		if 'USER_INPUT_DEPARTMENT' in request.session:
			print("app: USERS ->", request.session['USER_INPUT_DEPARTMENT'])
		'''
		
		return redirect(reverse('portfolios:index')) ###
	return render(request, 'registration/get_user_info.html', locals())