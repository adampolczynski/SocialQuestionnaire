from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from main.views import index

urlpatterns = patterns('',
	url(r'^$', index),
    # Examples:
    # url(r'^$', 'questions.views.home', name='home'),
    # url(r'^questions/', include('questions.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
