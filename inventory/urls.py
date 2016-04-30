from django.conf.urls import patterns, url

import inventory.views as iventory_view

urlpatterns = patterns('',
     url(r'overview/$', iventory_view.overview, name="inventory-list"),
     url(r'discover/$', iventory_view.discover, name="inventory-discover"),
     url(r'details/(?P<object_id>[0-9]+)$', iventory_view.details),
     url(r'object$', iventory_view.create, name="inventory-submit"),

     url(r'cloud', iventory_view.cloud, name='inventory-cloud'),
)