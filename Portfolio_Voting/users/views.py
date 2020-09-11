from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from users.models import User

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', locals())
    elif request.method == 'POST':
        return redirect(reverse('users:verify'))

def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))

@csrf_exempt
def verify(request):
    id = request.POST['id']
    type = request.POST['type']
    state = request.POST['state']

    USER_EXIST = len(User.objects.all().filter(username=id))
    #print(USER_EXIST)
    if USER_EXIST == 1 and type == '1' and state == '1':
        user = auth.authenticate(username=id, password=type)
        auth.login(request, user)
        return redirect(reverse('index'))

    elif USER_EXIST == 1 and type == '2' and state == '1':
        user = auth.authenticate(username=id, password=state)
        auth.login(request, user)
        return redirect(reverse('index'))

    elif USER_EXIST != 1 and type == '1' and state == '1':
        NEW_USER_RECORD = User.objects.create(username=id, is_active=True, is_admin=False)
        NEW_USER_RECORD.set_password(type)
        NEW_USER_RECORD.save()
        #print(NEW_USER_RECORD)
        user = auth.authenticate(username=id, password=type)
        auth.login(request, user)
        return redirect(reverse('index'))

    elif USER_EXIST != 1 and type == '2' and state == '1':
        NEW_USER_RECORD = User.objects.create(username=id, is_active=True, is_admin=False)
        NEW_USER_RECORD.set_password(state)
        NEW_USER_RECORD.save()
        #print(NEW_USER_RECORD)
        user = auth.authenticate(username=id, password=state)
        auth.login(request, user)
        return redirect(reverse('index'))
        #return render(request, 'test.html', {'id':id, 'type':type, 'state':state, 'username':username, 'password':password})

    else:
        return HttpResponse('Login Error!')
