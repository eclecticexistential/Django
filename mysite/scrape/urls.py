from django.urls import path
from . import views

app_name = 'scrape'
urlpatterns = [
	path('',views.index,name='index'),
	path('add/', views.add_urls, name='add_urls'),
	path('<int:url_id>/', views.detail, name='detail'),
]