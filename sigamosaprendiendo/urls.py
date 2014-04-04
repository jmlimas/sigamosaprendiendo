from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from apps.inicio.views import index


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sigamosaprendiendo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   # url(r'^', include('apps.inicio.urls')),
    url(r'^$','apps.inicio.views.index'),
)
