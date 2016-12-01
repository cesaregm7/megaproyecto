from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^record$', views.record, name='record_manager'),
    url(r'^statistics$', views.record_statistics, name='record_statistics'),
    url(r'^dashboard$', views.record_dashboard, name='record_dashboard'),
    url(r'^record/(?P<r>\d+)/(?P<r_id>[\w\-]+)$', views.record, name='record'),
    url(r'^record_view/(?P<r>\d+)/(?P<r_id>[\w\-]+)/(?P<f_id>\d+)$', views.record_view, name='url_record_view'),
    url(r'^file_view/(?P<r>\d+)/(?P<r_id>[\w\-]+)/(?P<f_id>\d+)/(?P<f_name>[\w\-]+)$', views.file_view, name='file_view'),
    url(r'^picture_view/(?P<field_id>\d+)$', views.picture_view, name='picture_view'),
    url(r'^record_edit/(?P<r>\d+)/(?P<r_id>[\w\-]+)/(?P<f_id>\d+)$', views.record_edit, name='record_edit'),
    url(r'^add_form/(?P<r>\d+)/(?P<r_id>[\w\-]+)$', views.form_add, name='form_add'),
    url(r'^save_form/(?P<r>\d+)/(?P<r_id>[\w\-]+)/(?P<f_id>\d+)$', views.save_form, name='save_form'),
    url(r'^add_file/(?P<r>\d+)/(?P<r_id>[\w\-]+)/(?P<f_id>\d+)$', views.add_file, name='add_file'),
    url(r'^remove_file/(?P<r>\d+)/(?P<r_id>[\w\-]+)$', views.remove_file, name='remove_file'),
    url(r'^add_summary/(?P<r>\d+)/(?P<r_id>[\w\-]+)/(?P<f_id>\d+)$', views.add_summary, name='add_summary'),
    url(r'^edit_summary/(?P<r>\d+)/(?P<r_id>[\w\-]+)/(?P<f_id>\d+)$', views.edit_summary, name='edit_summary'),
    url(r'^new_record$', views.new_record, name='new_record'),
    url(r'^add_comment/(?P<r>\d+)/(?P<r_id>[\w\-]+)/(?P<f_id>\d+)$', views.add_comment, name='add_comment'),
    url(r'^client_view/(?P<f_id>\d+)$', views.record_view_client, name='record_view_client'),
    url(r'^client_add_form$', views.form_add_client, name='form_add_client'),
    url(r'^client_save_form/(?P<f_id>\d+)$', views.save_form_client, name='save_form_client'),
    url(r'^client_record_edit/(?P<f_id>\d+)$', views.record_edit_client, name='record_edit_client'),
]
