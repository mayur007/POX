from django.conf.urls import patterns, include, url
from pockettracker.api.resources import MyModelResource
from tastypie.api import Api
#from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(MyModelResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pockettracker.views.index'),
    url(r'^(?P<category>[\w\-]+)/$', 'pockettracker.views.pocketdatas'),
    url(r'^api/', include(v1_api.urls)),
)
