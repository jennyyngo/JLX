from django.conf.urls import patterns, url
from GrubHunt import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^update/$', views.update, name='update'),
    url(r'^vendors/$', views.vendors, name='vendors'),
	url(r'^find_route/(?P<vendor_slug>[\w\-]+)/$',views.find_route, name='find_route'),
	url(r'^list_vendors/$', views.list_vendors, name='list_vendors'),
    )