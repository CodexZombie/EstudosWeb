# ../connectedin/
# ../perfis/urls.py

from django.conf.urls import patterns, url
from perfis.views import index, exibir

urlpatterns = patterns('',
    url(r'^$', 'perfis.views.index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir')
)
