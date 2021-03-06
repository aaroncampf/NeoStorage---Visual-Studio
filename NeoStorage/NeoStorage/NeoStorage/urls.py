"""
Definition of urls for NeoStorage.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()


urlpatterns = [# Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentat ion:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	
    #Aaron
    url(r'^locations$', app.views.locations, name='locations'),
	url(r'^location/(?P<pk>\d+)/$', app.views.LocationUpdate.as_view(), name='location'),
	url(r'^location/create/$', app.views.LocationCreate.as_view(), name='location-create'),
    url(r'^locationguide$', app.views.locationguide, name='locationguide'),

    url(r'^products$', app.views.products, name='products'),
	url(r'^product/(?P<pk>\d+)/$', app.views.ProductUpdate.as_view(), name='product'),
	url(r'^product/create/$', app.views.ProductCreate.as_view(), name='product-create'),

    url(r'^vendors$', app.views.vendors, name='vendors'),
	url(r'^vendor/(?P<pk>\d+)/$', app.views.VendorUpdate.as_view(), name='vendor'),
	url(r'^vendor/create/$', app.views.VendorCreate.as_view(), name='vendor-create')]

