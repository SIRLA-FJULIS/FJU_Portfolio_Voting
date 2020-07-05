from django.urls import path, include
from . import views

from django.views.generic.base import TemplateView

app_name = 'users'

urlpatterns = [
	path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    

    path('get_user_info/', views.get_user_info, name='get_user_info')
]


'''
# User 註冊頁面
http://127.0.0.1:8000/users/register/

# User 登入頁面
http://127.0.0.1:8000/users/accounts/login/ 

'''