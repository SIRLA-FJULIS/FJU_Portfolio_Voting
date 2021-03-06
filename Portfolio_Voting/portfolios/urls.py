from django.urls import path
from . import views

app_name = 'portfolios'

urlpatterns = [
    path('<str:college>', views.index, name='index'),
	path('work/<int:portfolio_id>', views.article, name='article'),
	path('work/<int:portfolio_id>/vote/', views.vote, name='vote'),
]