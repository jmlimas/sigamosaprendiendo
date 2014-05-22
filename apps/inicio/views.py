from django.shortcuts import render
from django.views.generic import TemplateView

#from apps.inicio.models import Alumno
  
class AboutView(TemplateView):
	template_name = 'home/about.html' 

class AnteView(TemplateView):
	template_name = 'home/antecedentes.html'

class RegionView(TemplateView):
	template_name = 'home/region.html'

class PropoView(TemplateView):
	template_name = 'home/propo.html'

class ObjeView(TemplateView):
	template_name = 'home/obje.html' 

class UbicaView(TemplateView):
	template_name = 'home/ubica.html'  

class EstView(TemplateView):
	template_name = 'home/estructura.html' 

class EstadisticaView(TemplateView):
	template_name='home/estadistica.html'

class NewsViews(TemplateView):
	template_name='home/news.html'

class OrgagramaViews(TemplateView):
	template_name = 'home/organigrama.html'

class GaleriaViews(TemplateView):
	template_name = 'home/galeria.html'

class ContactoViews(TemplateView):
	template_name = 'home/contactanos.html'

class NormaView(TemplateView):
	template_name = 'home/norma.html'
  
class MatView(TemplateView):
	template_name='home/materiales.html'