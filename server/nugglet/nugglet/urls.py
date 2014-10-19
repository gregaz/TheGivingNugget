from django.conf.urls import patterns, include, url
from django.contrib import admin
from NugAccount.views import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import login

urlpatterns = patterns('',
	('^logout/$', logout_view),
	('^amILoggedIn/', am_I_logged_in),
	('^accounts/profile/$', NugAccount_loggedInBalance),
	('^accounts/give/$', NugAccount_give),
	('^accounts/linkedAccount/$', NugAccount_setLinkedAccount),
	('^NugAccount/', include('NugAccount.urls')),
	(r'^login/$', csrf_exempt(login), {'template_name': 'login.html'}, 'login'),
	url(r'^admin/', include(admin.site.urls))
)