from django.urls import path
from . import views

app_name = 'portfolios'

urlpatterns = [
    path('<str:college>', views.index, name='index'),
	path('work/<int:portfolio_id>', views.article, name='article'),
	path('<int:choiceText_id>/results/', views.results, name='results'),
	path('<int:choiceText_id>/vote/', views.vote, name='vote'),
]