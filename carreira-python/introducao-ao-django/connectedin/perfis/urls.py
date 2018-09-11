# ../connectedin/
# ../perfis/urls.py

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'perfis.views.index')
)
