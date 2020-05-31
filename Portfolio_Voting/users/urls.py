from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]


'''
# User 註冊頁面
http://127.0.0.1:8000/users/register/

# User 登入頁面
http://127.0.0.1:8000/users/accounts/login/ 

'''