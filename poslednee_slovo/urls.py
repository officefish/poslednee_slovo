from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from lib.views import login

urlpatterns = patterns('',
    # Examples:
    (r'^crossdomain.xml', 'game.views.crossdomain'),


    # url(r'^$', 'poslednee_slovo.views.home', name='home'),
    # url(r'^poslednee_slovo/', include('poslednee_slovo.foo.urls')),
    url(r'^accounts/login/$', login,
                           {'template_name': 'registration/login.html'}),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url(r'^cards/', include('card.urls'), name='cards'),
     url(r'^heroes/', include('hero.urls'), name='heroes'),

)
