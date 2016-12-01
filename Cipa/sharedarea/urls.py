from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login_user'),
    url(r'^logout$', views.logout_user, name='logout_user'),
    url(r'^evaluar_test1$', views.evaluar_test1, name='evaluar_test1'),
    url(r'^evaluar_test2$', views.evaluar_test2, name='evaluar_test2'),
    url(r'^evaluar_test3$', views.evaluar_test3, name='evaluar_test3'),
    url(r'^evaluar_test4$', views.evaluar_test4, name='evaluar_test4'),
    url(r'^herramientas$', views.herramientas, name='herramientas'),
    url(r'^organizaciones$', views.servicio_organizaciones, name='organizaciones'),
    url(r'^educativo$', views.servicio_educativo, name='educativo'),
    url(r'^clinica$', views.servicio_psicoterapia, name='clinica'),
    url(r'^induccion/$', views.induccion_intro, name='induccion_intro'),
    url(r'^calendario/$', views.calendario, name='calendario'),
    url(r'^modulo_1$', views.induccion_modulo1, name='induccion_modulo1'),
    url(r'^modulo_2$', views.induccion_modulo2, name='induccion_modulo2'),
    url(r'^modulo_3$', views.induccion_modulo3, name='induccion_modulo3'),
    url(r'^modulo_4$', views.induccion_modulo4, name='induccion_modulo4'),
    url(r'^diploma$', views.generar_diploma, name='generar_diploma'),
    url(r'^test_modulo1$', views.test_modulo1, name='test_modulo1'),
    url(r'^test_modulo2$', views.test_modulo2, name='test_modulo2'),
    url(r'^test_modulo3$', views.test_modulo3, name='test_modulo3'),
    url(r'^test_modulo4$', views.test_modulo4, name='test_modulo4'),
    url(r'^fichas_tecnicas$', views.fichas_tecnicas, name='fichas_tecnicas'),
]
