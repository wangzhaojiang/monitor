from django.conf.urls import patterns, include, url

from django.contrib import admin
from monitor.state import views
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),
    #url(r'^info/$', views.info),
)
