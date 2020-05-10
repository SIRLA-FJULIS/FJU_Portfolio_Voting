from django.shortcuts import render
from portfolios.models import Work

def index(request):
	work_list = Work.objects.all()
	return render(request, 'index.html', {'work_list': work_list})