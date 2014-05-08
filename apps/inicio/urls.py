from django.conf.urls import patterns, include, url

from .views import AboutView,EstView,EstadisticaView,NewsViews,OrgagramaViews,GaleriaViews,ContactoViews
from .views import AnteView,RegionView,PropoView,ObjeView,UbicaView

urlpatterns = patterns('',
	url(r'^about/$',AboutView.as_view(),name = 'about'),
	url(r'^ante/$',AnteView.as_view(),name = 'ante'),
	url(r'^region/$',RegionView.as_view(),name = 'region'),
	url(r'^proposito/$',PropoView.as_view(),name = 'propo'),
	url(r'^objetivo/$',ObjeView.as_view(),name = 'obje'),
	url(r'^ubica/$',UbicaView.as_view(),name = 'ubica'),	
	url(r'^estructura/$',EstView.as_view(),name= 'estructura'),
	url(r'^estadistica/$',EstadisticaView.as_view(),name='estadistica'),
	url(r'^news/$',NewsViews.as_view(),name = 'news'),
	url(r'^galeria/$',GaleriaViews.as_view(),name ='gale'),
	url(r'^organigrama/$',OrgagramaViews.as_view(),name = 'news'),
	url(r'^contacto/$',ContactoViews.as_view(),name='contacto'),
) 