# -*- coding: utf-8 -*-

from django import forms
from  sharedarea.models import *
from django.db.models.fields import BLANK_CHOICE_DASH


generos = [('Female','Femenino'), 
		('Male','Masculino')]
edades =[('20 a 25 años','20 a 25 años'), 
		('26 a 30 años','26 a 30 años'),
		('31 a 35 años ','31 a 35 años'),
		('36 a 40 años','36 a 40 años'),
		('41 a 45 años','41 a 45 años'),
		('46 a 50 años','46 a 50 años'),
		('51 a 55 años','51 a 55 años'),
		('61 o mayor','61 o mayor')]

estado_civil = [('Soltero/a', 'Soltero/a'),
				('Casado/a', 'Casado/a')]

escolaridad = [('Primaria','Primaria'), 
		('Básicos','Básicos'),
		('Diversificado','Diversificado'),
		('Universidad','Universidad'),
		('Maestría','Maestría'),
		('Doctorado','Doctorado')]

tiempo_laboral = [('0 a 3 años', '0 a 3 años'),
				   ('4 a 7 años', '4 a 7 años'),
				   ('8 años o más', '8 años o más')]

size = [('Pequeña', 'Pequeña'),
		('Mediana', 'Mediana'),
		('Grande', 'Grande')]
tipo_empresa = [('Producción', 'Producción'),
				('Consumo Masivo', 'Consumo Masivo'),
				('Operaciones', 'Operaciones'),
				('Servicio', 'Servicio'),
				('Manufactura', 'Manufactura')]

relacion = [('parent', 'Padre/Madre'),
			('tutor', 'Tutor/Tutora'),
			('teachr', 'Maestro/Maestra')]

class TestGeneralForm(forms.ModelForm):
	class Meta:
		model = TestOrganizationGeneralForm
		exclude = ['test_result_id_test_result']
	def __init__ (self, *args, **kwargs):
		super(TestGeneralForm, self).__init__(*args, **kwargs)
		self.fields['name'] =  forms.CharField(label='Nombre', required= True,widget=forms.TextInput(attrs={'class':'form-control'}))
		self.fields['last_name'] =  forms.CharField(label='Apellido', required= True,widget=forms.TextInput(attrs={'class':'form-control'}))
		self.fields['age'] =  forms.IntegerField(label='Edad', min_value=1,widget=forms.NumberInput(attrs={'class':'form-control'}))
		self.fields['job'] =  forms.CharField(label='Departamento o área donde labora', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
		self.fields['gender'] = forms.ChoiceField(label='Genero',choices=generos, widget=forms.RadioSelect())
		self.fields['marital_status'] = forms.ChoiceField(label='Estado Civil',choices=estado_civil, widget=forms.RadioSelect())
		self.fields['education'] = forms.ChoiceField(label='Educacion',choices=escolaridad, widget=forms.RadioSelect())
		self.fields['working_time'] = forms.ChoiceField(label='Tiempo de laborar en la empresa',choices=tiempo_laboral, widget=forms.RadioSelect())
		self.fields['organization_size'] = forms.ChoiceField(choices=size, widget=forms.RadioSelect())
		self.fields['organization_type'] = forms.ChoiceField(label='Tipo de Organizacion',choices=tipo_empresa, widget=forms.RadioSelect())

class TestDemograficForm(forms.ModelForm):
	class Meta:
		model = TestDemograficResult
		exclude = ('id_test_demografic_result', 'test_result_id_test_result', 'test_id_test', 'result')
	def __init__ (self, *args, **kwargs):
		super(TestDemograficForm, self).__init__(*args, **kwargs)
		self.fields['gender'] = forms.ChoiceField(choices=BLANK_CHOICE_DASH + generos, 
												  widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['age'] = forms.IntegerField(min_value=1,
												widget=forms.NumberInput(attrs={'class':'form-control'}))
		self.fields['relationship'] = forms.ChoiceField(choices=BLANK_CHOICE_DASH + relacion,
														widget=forms.Select(attrs={'class':'form-control'}))
