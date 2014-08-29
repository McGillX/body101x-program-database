from django.conf.urls import patterns, url

from programs import views

urlpatterns = patterns('',
    url(r'^form/?', views.add_program, name='form'),
    url(r'^$', views.index, name='index')
)
