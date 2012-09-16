from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Torverwaltung.views.test'),
    url(r'^stats/', include('Torverwaltung.urls')),
    # url(r'^Froschbachtal/', include('Froschbachtal.foo.urls')),
    # (r'^comments/', include('django.contrib.comments.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
)
