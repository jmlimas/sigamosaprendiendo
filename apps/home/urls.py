from django.conf.urls import patterns,url
from .views import IndexView

urlpatterns = patterns('',
	url(r'^$',IndexView.as_view(),name = 'index'),	
	url(r'^contacto/$','apps.home.views.contacto_view',name= 'vista_contacto'),
)