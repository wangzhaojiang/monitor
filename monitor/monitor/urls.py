from django.conf.urls import patterns, include, url

from django.contrib import admin
from monitor.state import views
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),
    #url(r'^get_cpu/$', views.get_cpu),
    url(r'^get_port/$', views.get_port),
    #url(r'^get_memory/$', views.get_memory),
    url(r'^state/$', views.state),
    url(r'^network/$', views.state_netstat),
    #url(r'^cpu/$', views.state_cpu),
    #url(r'^memory/$', views.state_memory),
    
)
