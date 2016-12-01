from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
#    url(r'^record$', views.record, name='record_manager'),
#    url(r'^dashboard$', views.record_dashboard, name='record_dashboard'),
#    url(r'^record_view/(?P<r_id>[\w\-]+)$', views.record_view, name='record_view'),
#    url(r'^save_form$', views.save_form, name='save_form'),
	url(r'^update_user_profile/(?P<pk>\d+)$', views.update_user_profile, name='update_user_profile'),
	url(r'^view_user_profile/(?P<pk>\d+)$', views.view_user_profile, name='view_user_profile'),
	url(r'^list_user_profiles$', views.list_user_profiles, name='list_user_profiles'),
	url(r'^pdf_template.pdf/(?P<pk>\d+)$', views.pdf_template, name='pdf_template.pdf'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
