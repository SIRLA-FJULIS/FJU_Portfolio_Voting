from django.shortcuts import render
from django.urls import reverse

from portfolios.models import Work

def index(request):
	return render(request, 'index.html')