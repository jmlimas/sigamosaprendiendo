from django.conf.urls import patterns, include, url
<<<<<<< HEAD
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
 
=======

from django.contrib import admin
admin.autodiscover()

from apps.inicio.views import index
>>>>>>> 2cf06878d7ea69d846cbf3821250260cce6c9faf


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sigamosaprendiendo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^',include('apps.home.urls')), 
    url(r'^',include('apps.inicio.urls',namespace='inicio')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT,}
        ),
)
=======
   # url(r'^', include('apps.inicio.urls')),
    url(r'^$','apps.inicio.views.index'),
)
>>>>>>> 2cf06878d7ea69d846cbf3821250260cce6c9faf
