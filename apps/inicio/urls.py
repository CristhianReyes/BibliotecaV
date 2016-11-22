from django.conf.urls import patterns, include, url
from .views import index, index2

urlpatterns = patterns('',


url(r'^$', index.as_view()),
url(r'^index/$', index2.as_view()),

)
