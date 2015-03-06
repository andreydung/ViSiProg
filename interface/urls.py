from django.conf.urls import patterns, include, url
from interface.views import *

urlpatterns = patterns('',
    url(r'^$', interface_page),
    url(r'^test/$', test_page),
    url(r'^groups/$', groups_page),
)