from django.conf.urls import patterns, url, include
from GrubHunt import views
from GrubHunt.forms import UserProfileForm


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^update/$', views.update, name='update'),
    url(r'^vendors/$', views.vendors, name='vendors'),
	url(r'^find_route/(?P<vendor_slug>[\w\-]+)/$',views.find_route, name='find_route'),
	url(r'^list_vendors/$', views.list_vendors, name='list_vendors'),
	url(r'^profile/(?P<userprofile_slug>[\w\-]+)/$',views.profile, name='profile'),
	url(r'^profile/(?P<userprofile_slug>[\w\-]+)/edit_profile/$',views.edit_profile, name='edit_profile'),
	url(r'^find_route/(?P<vendor_slug>[\w\-]+)/add_vendor_to_user/$',views.add_vendor_to_user, name='add_vendor_to_user'),
	url(r'^profile/(?P<userprofile_slug>[\w\-]+)/remove_vendor/(?P<vendor_slug>[\w\-]+)/$', views.remove_vendor, name='remove_vendor'),
    url('', include('social.apps.django_app.urls', namespace='social'))
)