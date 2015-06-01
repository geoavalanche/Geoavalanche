from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *

urlpatterns = patterns('',
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
#	url(r'^thanks/$', 'geoavalanche.views.thanks', name='thanks'),
#   url(r'^[\w+]+/thanks/$', 'geoavalanche.views.thanks', name='thanks'),
   url(r'^contact/$', 'geoavalanche.views.contactus', name='contactus'),
   url(r'^[\w+]+/contact/$', 'geoavalanche.views.contactus', name='contactus'),
#   url(r'^thanks/$', 'geoavalanche.views.thanks', name='thanks'),
#   url(r'^mymodal/', MyModal.as_view(), name='mymodal'),
 ) + urlpatterns
