from django.urls import path
from . import views

app_name = 'portfolios'

urlpatterns = [
    path('<str:college>', views.index, name='index'),
	path('<int:choiceText_id>/', views.detail, name='detail'),
	path('<int:choiceText_id>/results/', views.results, name='results'),
	path('<int:choiceText_id>/vote/', views.vote, name='vote'),
]