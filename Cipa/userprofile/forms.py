# -*- coding: utf-8 -*-
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from sorl.thumbnail import get_thumbnail
from django import forms
from sharedarea.models import *
from django.forms import extras



bajo = 0
regular = 1
bueno = 2
excelente = 3
options = [(bajo, 'Bajo'),
			(regular, 'Regular'),
			(bueno, 'Bueno'),
			(excelente, 'Excelente')]
class AdminImageWidget(AdminFileWidget):
  def render(self, name, value, attrs={'class': 'btn-default'}):
    output = []
    if value and getattr(value, "url", None):
    	t = get_thumbnail(value,'200x200')
    	output.append('<img class="img-rounded" style="margin-bottom: 15px" src="{}">'.format(t.url))
    output.append(super(AdminFileWidget, self).render(name, attrs))
    return mark_safe(u''.join(output))


class UserDataForm(forms.ModelForm):
	class Meta:
		model = AuthUser
		fields = '__all__'
	def __init__ (self, *args, **kwargs):
		super(UserDataForm, self).__init__(*args, **kwargs)
		self.fields['image_uri'] = forms.ImageField(label='Imagen', required=False, widget=AdminImageWidget())
		self.fields['quote'] = forms.CharField(label='Cita', required=False,  widget=forms.Textarea(attrs={'class':'form-control'}))
		self.fields['password'] = forms.CharField(label='', required=False, widget = forms.HiddenInput())
		self.fields['last_login'] = forms.DateTimeField(label='', required=False, widget = forms.HiddenInput())
		self.fields['is_superuser'] = forms.IntegerField(label='', required=False, widget = forms.HiddenInput())
		self.fields['username'] =  forms.CharField(label='Usuario', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
		self.fields['first_name'] =  forms.CharField(label='Nombre', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
		self.fields['last_name'] = forms.CharField(label='Apellido', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
		self.fields['email'] = forms.CharField(label='Correo', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
		self.fields['is_staff'] = forms.IntegerField(label='', required=False, widget = forms.HiddenInput())
		self.fields['is_active'] = forms.IntegerField(label='', required=False, widget = forms.HiddenInput())
		self.fields['date_joined'] = forms.DateTimeField(label='', required=False, widget = forms.HiddenInput())
		self.fields['role_user'] = forms.IntegerField(label='', required=False, widget = forms.HiddenInput())
		self.fields['birthdate'] = forms.DateField(label='Nacimiento', required=False, widget=forms.TextInput(attrs={'class':'form-control','data-format':'YYYY-MM-DD', 'data-template':'YYYY MM DD'}))
		self.fields['country'] = forms.CharField(label='País', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
		



class UserSkillForm(forms.ModelForm):
	class Meta:
		model = UserSkills
		fields = '__all__'
	def __init__ (self, *args, **kwargs):
		super(UserSkillForm, self).__init__(*args, **kwargs)
		self.fields['computer_skill'] = forms.ChoiceField(choices=options, label='Destreza en el uso de la computadora',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['learning_skill'] = forms.ChoiceField(choices=options, label='Compromiso de aprender',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['ethic_skill'] = forms.ChoiceField(choices=options, label='Compromiso ético',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['responsability_skill'] = forms.ChoiceField(choices=options,label='Responsabilidad',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['strategy_skill'] = forms.ChoiceField(choices=options,label='Estrategia Profesional',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['professional_growth_skill'] = forms.ChoiceField(choices=options,label='Desarrollo profesional continuo',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['professional_relationships_skill'] = forms.ChoiceField(choices=options,label='Relaciones profesionales ',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['interpersonal_relationships_skill'] = forms.ChoiceField(choices=options,label='Relaciones interpersonales ',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['knowledge_skill'] = forms.ChoiceField(choices=options,label='Aplicación de conocimientos ',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['problem_solver_skill'] = forms.ChoiceField(choices=options,label='Solución de problemas',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['effective_communication_skill'] = forms.ChoiceField(choices=options,label='Comunicación efectiva',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['control_skill'] = forms.ChoiceField(choices=options,label='Control',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['adaptability_skill'] = forms.ChoiceField(choices=options,label='Adaptabilidad',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['creativity_skill'] = forms.ChoiceField(choices=options,label='Creatividad',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['decision_making_skill'] = forms.ChoiceField(choices=options,label='Toma de Decisiones',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['emotional_skill'] = forms.ChoiceField(choices=options,label='Inteligencia Emocional',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['opportunity_identification_skill'] = forms.ChoiceField(choices=options,label='Identificacion de oportunidades',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['team_work_skill'] = forms.ChoiceField(choices=options,label='Trabajo en equipo',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['leadership_skill'] = forms.ChoiceField(choices=options,label='Liderazgo',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['conflict_manage_skill'] = forms.ChoiceField(choices=options,label='Manejo de conflictos',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['proactivity'] = forms.ChoiceField(choices=options,label='Proactividad',widget=forms.Select(attrs={'class':'form-control'}))
		self.fields['auth_user'].widget = forms.HiddenInput()

