from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from apps.inicio.forms import CanaForm
from django.core.mail import EmailMultiAlternatives # Enviamos HTML

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



def cana_view(request):
	info_enviado  =  False
	escuela   = ""
	turno     = ""
	clave     = ""
	zona      = ""
	dirEscl   = ""
	telEsc	  = ""
	maestro   = "" 
	email     = ""
	apoyo     = ""
	porque    = ""
	alumno    = ""
	fechaNci  = ""
	edad      = ""
	grado     = ""
	dirAlumno = ""
	telAlumno = ""
	amigo1    = ""
	amigo2    = ""
	fechaEnfe = ""
	nomMadre  = ""
	nomPadre  = ""
	if request.method =="POST":
		formulario = CanaForm(request.POST)
		if formulario.is_valid():
			info_enviado = True						 
			escuela   = formulario.cleaned_data['Escuela']
			turno     = formulario.cleaned_data['Turno']
			clave     = formulario.cleaned_data['Clave']
			zona      = formulario.cleaned_data['Zona']
			dirEscl   = formulario.cleaned_data['DirEscl']
			telEsc	  = formulario.cleaned_data['TelEsc']
			maestro   = formulario.cleaned_data['Maestro'] 
			email     = formulario.cleaned_data['Email']
			apoyo     = formulario.cleaned_data['Apoyo']
			porque    = formulario.cleaned_data['Porque']
			alumno    = formulario.cleaned_data['Alumno']
			fechaNci  = formulario.cleaned_data['FechaNci']
			edad      = formulario.cleaned_data['Edad']
			grado     = formulario.cleaned_data['Grado']
			dirAlumno = formulario.cleaned_data['DirAlumno']
			telAlumno = formulario.cleaned_data['TelAlumno']
			amigo1    = formulario.cleaned_data['Amigo1']
			amigo2    = formulario.cleaned_data['Amigo2']
			fechaEnfe = formulario.cleaned_data['FechaEnfe']
			nomMadre  = formulario.cleaned_data['NomMadre']
			nomPadre  = formulario.cleaned_data['NomPadre']

			# Configuracion enviando mensaje via GMAIL
			to_admin = 'sigamosaprendiendolaguna@gmail.com'
			html_content = "Escuela[%s]<br>Turno[%s]<br>Clave[%s]<br>zona[%s]<br>dirEscl[%s]<br>TelEsc[%s]<br>Maestro[%s]<br>email[%s]<br>apoyo[%s]<br>porque[%s]<br>alumno[%s]<br>fechaNci[%s]<br>edad[%s]<br>grado[%s]<br>dirAlumno[%s]<br>telAlumno[%s]<br>amigo1[%s]<br>amigo2[%s]<br>fechaEnfe[%s]<br>nomMadre[%s]<br>nomPadre%s"%(escuela,turno,clave,zona,dirEscl,telEsc,maestro,email,apoyo,porque,alumno,fechaNci,edad,grado,dirAlumno,telAlumno,amigo1,amigo2,fechaEnfe,nomMadre,nomPadre)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') # Definimos el contenido como HTML
			msg.send() # Enviamos  en correo
			print 'si entro'
	else:
		print 'no entro'
		formulario = CanaForm()
	ctx = {'form':formulario,'escuela':escuela,'turno':turno,'clave':clave,'zona':zona,
	       'dirEscl':dirEscl,'telEsc':telEsc,'maestro':maestro,'email':email,'apoyo':apoyo,'porque':porque,
		    'alumno':alumno,'fechaNci':fechaNci,'edad':edad,'grado':grado,'dirAlumno':dirAlumno,
		    'telAlumno':telAlumno,'amigo1':amigo1,'amigo2':amigo2,'fechaEnfe':fechaEnfe,'nomMadre':nomMadre,
			'nomPadre':nomPadre,'info_enviado':info_enviado}
	return render_to_response('inicio/canaliza.html',ctx,context_instance=RequestContext(request))