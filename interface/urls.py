from django.conf.urls import patterns, include, url
from interface.views import *

urlpatterns = patterns('',
    url(r'^$', interface_page, name = 'index'),
    url(r'^test/$', test_page, name = 'test'),
    url(r'^groups/$', groups_page, name = 'group'),
    url(r'^groups/(?P<theusername>\w+)/$', groups_page),

    url(r'^testLLNL2/$', test_page_LLNL2, name = 'testLLNL2'),
    url(r'^groupsLLNL2/$', groups_page_LLNL2, name = 'groupLLNL2'),
    url(r'^groupsLLNL2/(?P<theusername>\w+)/$', groups_page_LLNL2),

    url(r'^testLLNL3/$', test_page_LLNL3, name = 'testLLNL3'),
    url(r'^groupsLLNL3/$', groups_page_LLNL3, name = 'groupLLNL3'),
    url(r'^groupsLLNL3/(?P<theusername>\w+)/$', groups_page_LLNL3),

)