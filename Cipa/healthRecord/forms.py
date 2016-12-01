# -*- coding: utf-8 -*-
from django import forms
from sharedarea.models import *
from healthRecord.field import *
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.db.models import Q

servicios_cipa = [('Psicoterapia','Psicoterapia'), 
		('Consejería','Consejería'),
		('Evaluación Psicológica','Evaluación Psicológica'),
		('Evaluación Psicoeducativa','Evaluación Psicoeducativa')]
lista_genero = [('F','Femenino'), 
		('M','Masculino'),
		('Otros','Otros')]
lista_escolaridad = [('Prescolar','PRESCOLAR: Pre-Kinder, Kinder (Párvulos), Prepa'),('Primaria','PRIMARIA: Primero, Segundo, Tercero, Cuarto, Quinto, Sexto'),
		('Básicos','BÁSICOS: Primero, Segundo, Tercero'),('Diversificado','DIVERSIFICADO: Cuarto, Quinto, Sexto'),('Universitario','UNIVERSITARIO: Pregrado, Postgrado')]
lista_estatus = [('Referido','Referido'),('En Proceso','En Proceso'), ('De Baja','De Baja')]
lista_tipo_servicio = [('CLI','Clínico'),('EDU','Educativo'),('CON','Consejería'),('NEU','Neuropsicología')]
lista_pruebas_aplicadas = []
lista_referido = [('Institución Educativa','Institución Educativa'), ('Institución de Salud','Institución de Salud'), 
				('Clientes de CIPA','Clientes de CIPA'), ('Estudiantes','Estudiantes'), ('Colaboradores UVG','Colaboradores UVG'), ('OTRO','OTRO')]

class recordForm(forms.ModelForm):
	record_type = forms.CharField(widget=forms.Select(choices=servicios_cipa))
	record_date = forms.DateField()
	professor_ids = User.objects.filter(groups__name='Catedrático')|User.objects.filter(groups__name='Administrador')
	professor = UserModelChoiceField(queryset=AuthUser.objects.filter(id__in=professor_ids), required=False)
	student_ids = User.objects.filter(groups__name='Estudiante')
	student = UserModelChoiceField(queryset=AuthUser.objects.filter(id__in=student_ids), required=False)
	class Meta:
		model = Record
		exclude = ['client_id_client']
	def __init__(self, *args, **kwargs):
		super(recordForm, self).__init__(*args, **kwargs)
		self.fields['record_type'].widget.attrs['class'] = 'form-control'
		self.fields['record_date'].widget.attrs['class'] = 'form-control'
		self.fields['professor'].widget.attrs['class'] = 'form-control'
		self.fields['student'].widget.attrs['class'] = 'form-control'
	
class fileUploadForm(forms.Form):
	file_to_upload = forms.FileField()
	
class fileUploadForm2(forms.Form):
	file_to_upload = forms.FileField()
	name_of_file = forms.CharField(required=False)
	def __init__(self, *args, **kwargs):
		super(fileUploadForm2, self).__init__(*args, **kwargs)
		self.fields['name_of_file'].widget.attrs['class'] = 'form-control'
		
class summaryForm(forms.ModelForm):
	gender = forms.CharField(widget=forms.Select(choices=lista_genero))
	birth_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
	age = forms.IntegerField()
	education = forms.CharField(widget=forms.Select(choices=lista_escolaridad))
	registration_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
	termination_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
	current_status = forms.CharField(widget=forms.Select(choices=lista_estatus))
	service_type = forms.CharField(widget=forms.Select(choices=lista_tipo_servicio))
	consultation_reason = forms.CharField(widget=forms.Textarea)
	applied_tests = forms.CharField(widget=forms.Textarea)
	number_sessions = forms.IntegerField()
	diagnosis = forms.CharField(widget=forms.Textarea)
	referred_by = forms.CharField(widget=forms.Select(choices=lista_referido))
	class Meta:
		model = SummaryForm
		exclude = ["record_id_record", "form_type_id_form_type"]
	def __init__(self, *args, **kwargs):
		super(summaryForm, self).__init__(*args, **kwargs)
		self.fields['gender'].widget.attrs['class'] = 'form-control'
		self.fields['birth_date'].widget.attrs['class'] = 'form-control date_picker'
		self.fields['age'].widget.attrs['class'] = 'form-control'
		self.fields['education'].widget.attrs['class'] = 'form-control'
		self.fields['registration_date'].widget.attrs['class'] = 'form-control date_picker'
		self.fields['termination_date'].widget.attrs['class'] = 'form-control date_picker'
		self.fields['current_status'].widget.attrs['class'] = 'form-control'
		self.fields['service_type'].widget.attrs['class'] = 'form-control'
		self.fields['consultation_reason'].widget.attrs['class'] = 'form-control'
		self.fields['applied_tests'].widget.attrs['class'] = 'form-control'
		self.fields['number_sessions'].widget.attrs['class'] = 'form-control'
		self.fields['diagnosis'].widget.attrs['class'] = 'form-control'
		self.fields['referred_by'].widget.attrs['class'] = 'form-control'
		self.fields['consultation_reason'].widget.attrs['placeholder'] = 'Seleccione de la lista (barra espaciadora para ver la lista completa)'
		self.fields['applied_tests'].widget.attrs['placeholder'] = 'Seleccione de la lista (barra espaciadora para ver la lista completa)'
		self.fields['diagnosis'].widget.attrs['placeholder'] = 'Seleccione de la lista (barra espaciadora para ver la lista completa)'
		
		
		self.fields['termination_date'].required = False
		self.fields['consultation_reason'].required = False
		self.fields['applied_tests'].required = False
		self.fields['diagnosis'].required = False
	
