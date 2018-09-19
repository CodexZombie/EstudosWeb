# ../connectedin/
# ../usuarios/urls.py

from django.conf.urls import patterns, url
from usuarios.views import RegistrarUsuarioView

urlpatterns = patterns('',
    url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar')
)