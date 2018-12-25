from django.urls import path
from . import views

app_name = 'odds'

urlpatterns = [
	path('', views.index, name='index'),
	path('playersearch/', views.player_search, name='player_search'),
	path('results/', views.results, name='results'),
]