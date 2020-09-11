from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from users.models import User

from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', locals())
    elif request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('pasw')
        #print(username, password)
        request.session['INPUT_STUDID'] = username
        request.session['INPUT_PASSWORD'] = password
        return redirect(reverse('users:verify'))

def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))

@csrf_exempt
def verify(request):
    username = request.session['INPUT_STUDID']
    password = request.session['INPUT_PASSWORD']
    #print(password, username)

    id = request.POST['id']
    type = request.POST['type']
    state = request.POST['state']

    if type == '1' and state == '1':
        NEW_USER_RECORD = User.objects.create(username=username, is_active=True, is_admin=False)
        NEW_USER_RECORD.set_password(password)
        NEW_USER_RECORD.save()
        #print(NEW_USER_RECORD)
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return redirect(reverse('index'))
        #return render(request, 'test.html', {'id':id, 'type':type, 'state':state, 'username':username, 'password':password})

    elif type == '2' and state == '1':
        NEW_USER_RECORD = User.objects.create(username=username, is_active=True, is_admin=False)
        NEW_USER_RECORD.set_password(password)
        NEW_USER_RECORD.save()
        #print(NEW_USER_RECORD)
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return redirect(reverse('index'))
        #return render(request, 'test.html', {'id':id, 'type':type, 'state':state, 'username':username, 'password':password})

    else:
        return HttpResponse('Login Error!')
    #NEW_USER_RECORD = User.objects.create(username=username, is_active=True, is_admin=False)
    #NEW_USER_RECORD.set_password(password)
    #NEW_USER_RECORD.save()
    #print(NEW_USER_RECORD)
