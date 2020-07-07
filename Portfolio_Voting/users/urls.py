from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
	path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]