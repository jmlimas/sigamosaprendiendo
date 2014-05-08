from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
 


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sigamosaprendiendo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('apps.home.urls')), 
    url(r'^',include('apps.inicio.urls',namespace='inicio')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT,}
        ),
)