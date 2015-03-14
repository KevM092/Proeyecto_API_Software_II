from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
	  url(r'^Cliente/$', 'api.views.Cliente_list', name='Cliente_list'),
    url(r'^Cliente/(?P<pk>[0-9]+)$', 'api.views.Cliente_detail', name='Cliente_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
