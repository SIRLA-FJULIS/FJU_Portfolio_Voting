from django.shortcuts import redirect
from django.urls import reverse

from portfolios.models import Work

def index(request):
	return redirect(reverse('portfolios:index', kwargs={'college': '文學院'}))