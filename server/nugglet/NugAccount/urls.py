from django.conf.urls import patterns
from NugAccount.views import *

urlpatterns = patterns('',
	('^$', NugAccount_list),
	('^account/(?P<NugAccount_name>.*)/$', NugAccount_balance),
	('^give/(?P<NugAccount_name>.*)/$', NugAccount_give),
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)