from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
	
	path('albums', views.index),
	path('artist/', views.listing, name = 'listing'),
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^search/$', views.search,name = 'search'),

]
