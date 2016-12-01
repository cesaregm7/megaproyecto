from django.conf.urls import url

from . import views

urlpatterns = [
#Pablo
    url(r'^consentimiento_test_preliminar/(?P<test>\d+)$', views.consentimiento_test_preliminar, name='consentimiento_test_preliminar'),
    url(r'^test_preliminar/(?P<test>\d+)$', views.test_preliminar, name='test_preliminar'),
	url(r'^test_result$', views.test_result, name='test_result'),
	url(r'^descargar_test$', views.descargar_test, name='descargar_test'),
    url(r'^formulario_demografico/(?P<test>\d+)$', views.formulario_demografico, name='formulario_demografico'),
#Kevin
    url(r'^test_organizaciones/(?P<test>\d+)$', views.test_organizaciones, name='test_organizaciones'),
    url(r'^consentimiento_informado/(?P<test>\d+)$', views.consentimiento_informado, name='consentimiento_informado'),
    url(r'^formulario_general/(?P<test>\d+)$', views.formulario_general, name='formulario_general'),
]
