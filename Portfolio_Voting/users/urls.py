from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'users'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('verify/', views.verify, name='verify'),
]
