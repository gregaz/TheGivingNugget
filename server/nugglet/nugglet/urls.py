from django.conf.urls import patterns, include, url
from django.contrib import admin
from NugAccount.views import *

urlpatterns = patterns('',
	('^logout/$', logout_view),
	('^amILoggedIn/', am_I_logged_in),
	('^accounts/profile/$', NugAccount_loggedInBalance),
	('^NugAccount/', include('NugAccount.urls')),
	url(r'^admin/', include(admin.site.urls))
)