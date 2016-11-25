from django.conf.urls import patterns, include, url
from .views import BuscarView, BusquedaView
from . import views

urlpatterns = patterns('',


url(r'^buscar/$', BuscarView.as_view(), name = 'buscar'),
url(r'^busqueda/$', BusquedaView.as_view()),
url(r'^libros/$', views.libro_lista, name = 'libro_lista'),
url (r'^libro/(?P<pk>[0-9]+)/$', views.libro_detalle, name='libro_detalle'),
url (r'^libro/new/$', views.libro_nuevo, name='libro_nuevo'),
url(r'^libro/(?P<pk>[0-9]+)/edit/$', views.libro_editar, name='libro_editar'),
url(r'^libro/(?P<pk>[0-9]+)/borrar/$', views.libro_eliminar, name='libro_eliminar'),
)
