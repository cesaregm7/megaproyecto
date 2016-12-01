from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^herramientas/subir$', views.subir_documento, name='subir_documento'),
    url(r'^herramientas/recomendaciones$', views.recomendaciones, name='recomendaciones'),
	url(r'^search/(?P<search>.{0,100})$', views.ver_busqueda_documento, name='ver_busqueda_documento'),
]
