from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
	 url(r'^Cliente/$', 'api.views.Cliente_list', name='Cliente_list'),
	 url(r'^Cliente/(?P<pk>[0-9]+)$', 'api.views.Cliente_detail', name='Cliente_detail'),
    
	url(r'^Evento/$', 'api.views.Evento_list', name='Evento_list'),
	url(r'^Evento/(?P<pk>[0-9]+)$', 'api.views.Evento_detail', name='Evento_detail'),
	
	url(r'^Categoria/$', 'api.views.Categoria_list', name='Categoria_list'),
	url(r'^Categoria/(?P<pk>[0-9]+)$', 'api.views.Categoria_detail', name='Categoria_detail'),
    
    url(r'^admin/', include(admin.site.urls)),
)
