from django.conf.urls import patterns, include, url
from .views import BuscarView, BusquedaView

urlpatterns = patterns('',


url(r'^buscar/$', BuscarView.as_view(), name = 'buscar'),
url(r'^busqueda/$', BusquedaView.as_view()),

)
