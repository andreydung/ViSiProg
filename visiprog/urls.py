from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'visiprog.views.home', name = 'home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name = 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/visiprog/'}, name = 'logout'),    
    url(r'^interface/', include('interface.urls', namespace = 'interface')),    
	url(r'^admin/', include(admin.site.urls)),
)
