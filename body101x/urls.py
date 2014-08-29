from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'body101x.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^programs/', include('programs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
