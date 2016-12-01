# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from sharedarea.models import *
from django.http import HttpResponse
from healthRecord.forms import *
from django.utils.dateparse import parse_date
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.conf import settings
from django.db.models import Q 
from mimetypes import MimeTypes
import urllib
from PIL import Image
from django.core.mail import EmailMessage
import string
import random

# Create your views here.

def record_statistics(request):
	if (not request.user.is_authenticated()):
		return redirect('/')
	if not request.user.groups.filter(name='Administrador').exists():
		return redirect('/herramientas')
	#------Genero
	num_f = SummaryForm.objects.filter(gender='F').count()
	num_m = SummaryForm.objects.filter(gender='M').count()
	num_o = SummaryForm.objects.filter(gender='Otros').count()
	list_gender_2 = [num_f,num_m,num_o]
	list_gender = ['Femenino', 'Masculino', 'Otro']
	tuple_gender = zip(list_gender,list_gender_2)
	
	#------Edad-----------------
	age_1 = SummaryForm.objects.filter(age__range=(3,7)).count()
	age_2 = SummaryForm.objects.filter(age__range=(8,12)).count()
	age_3 = SummaryForm.objects.filter(age__range=(13,15)).count()
	age_4 = SummaryForm.objects.filter(age__range=(16,20)).count()
	age_5 = SummaryForm.objects.filter(age__range=(21,30)).count()
	age_6 = SummaryForm.objects.filter(age__range=(31,40)).count()
	age_7 = SummaryForm.objects.filter(age__range=(41,50)).count()
	age_8 = SummaryForm.objects.filter(age__range=(51,60)).count()
	age_9 = SummaryForm.objects.filter(age__range=(61,70)).count()
	age_10 = SummaryForm.objects.filter(age__range=(71,80)).count()
	list_age_2 = [age_1,age_2,age_3,age_4,age_5,age_6,age_7,age_8,age_9,age_10]
	list_age = ['3-7', '8-12', '13-15', '16-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80']
	tuple_age = zip(list_age,list_age_2)
	
	#-----Escolaridad
	education_1 = SummaryForm.objects.filter(education='Prescolar').count()
	education_2 = SummaryForm.objects.filter(education='Primaria').count()
	education_3 = SummaryForm.objects.filter(education='Básicos').count()
	education_4 = SummaryForm.objects.filter(education='Diversificado').count()
	education_5 = SummaryForm.objects.filter(education='Universitario').count()
	list_education_2 = [education_1,education_2,education_3,education_4,education_5]
	list_education0 = ['PRESCOLAR: Pre-Kinder, Kinder (Párvulos), Prepa', 'PRIMARIA: Primero, Segundo, Tercero, Cuarto, Quinto, Sexto', 'BÁSICOS: Primero, Segundo, Tercero', 'DIVERSIFICADO: Cuarto, Quinto, Sexto', 'UNIVERSITARIO: Pregrado, Postgrado']
	list_education = ['PRESCOLAR', 'PRIMARIA', 'BÁSICOS', 'DIVERSIFICADO', 'UNIVERSITARIO']
	tuple_education = zip(list_education,list_education_2)
	
	#-----Estatus
	status_1 = SummaryForm.objects.filter(current_status='Referido').count()
	status_2 = SummaryForm.objects.filter(current_status='En Proceso').count()
	status_3 = SummaryForm.objects.filter(current_status='De Baja').count()
	list_status_2 = [status_1,status_2,status_3]
	list_status = ['Referido', 'En Proceso', 'De Baja']
	tuple_status = zip(list_status,list_status_2)
	
	#-----Tipo Servicio
	service_1 = SummaryForm.objects.filter(service_type='CLI').count()
	service_2 = SummaryForm.objects.filter(service_type='EDU').count()
	service_3 = SummaryForm.objects.filter(service_type='CON').count()
	service_4 = SummaryForm.objects.filter(service_type='NEU').count()
	list_service_2 = [service_1, service_2, service_3, service_4]
	list_service = ['Clínico', 'Educativo', 'Consejería', 'Neuropsicología']
	tuple_service = zip(list_service,list_service_2)
	
	#-----Referido
	referred_1 = SummaryForm.objects.filter(referred_by='Institución Educativa').count()
	referred_2 = SummaryForm.objects.filter(referred_by='Institución de Salud').count()
	referred_3 = SummaryForm.objects.filter(referred_by='Clientes de CIPA').count()
	referred_4 = SummaryForm.objects.filter(referred_by='Estudiantes').count()
	referred_5 = SummaryForm.objects.filter(referred_by='Colaboradores UVG').count()
	referred_6 = SummaryForm.objects.filter(referred_by='OTRO').count()
	list_referred_2 = [referred_1, referred_2, referred_3, referred_4, referred_5, referred_6]
	list_referred = ['Institución Educativa', 'Institución de Salud', 'Clientes de CIPA', 'Estudiantes', 'Colaboradores UVG', 'OTRO']
	tuple_referred = zip(list_referred,list_referred_2)
	
	#-----consultation
	list_consultation_1=["Trastorno Déficit de Atención","Trastorno Déficit de Atención con Hiperactividad","Autismo","Problemas de Aprendizaje","Déficit Intelectual","Admisión Académica","Habilidad General","Problemas del Habla","Problemas Escolares","Problemas Conductuales","Duelos","Divorcio","Dificultades Familiares","Manejo de Emociones","Relaciones Interpersonales","Trauma","Trastornos del Desarrollo","Trastorno Degenerativo","Anoxia","Epilepsia","Depresión","Ansiedad","Trastorno Obsesivo Compulsivo","Trastornos Alimentarios","Trastorno de la Personalidad","OTROS"]
	list_consultation_2=[]
	
	for elem in list_consultation_1:
		list_consultation_2.append(SummaryForm.objects.filter(consultation_reason__contains=elem).count())
	tuple_consultation = zip(list_consultation_1, list_consultation_2)
	tuple_consultation_sorted = sorted(tuple_consultation, key=lambda x: x[1], reverse=True)
	
	
	#------test
	list_test_1 = ["Differential Aptitude Scale (DAS)", "Test Breve de Inteligencia Kaufman (K.BIT)", "Stanford-Binet Intelligence Scale (Stanford-Binet)", "Escala de Inteligencia de Wechsler para adultos (WAIS)", "Escala de Inteligencia de Wechsler para Adultos (WAIS)", "Escala de Inteligencia Wechsler para Adultos (EIWA)", "Escala de Inteligencia Wechsler para Adultos (WAIS-IV)", "Escala de Inteligencia de Wechsler para Niños (WISC-R)", "Escala Wechsler de Inteligencia para Niños (WISC-III)", "Escala de Inteligencia Wechsler para Niños (WISC-IV)", "Escala de Inteligencia de Wechsler para Preescolares(WPPSI-III)", "Escala de inteligencia de Wechsler para pre escolares (WPPSI-R)", "Escala de Inteligencia para los niveles pre escolares y primarios (WPPSI)", "Columbia Mental Maturity Scale (CMMS)", "Boehm Test of Basic Concepts (Boehm-3)", "Culture Fair Intelligence Test (Factor G)", "Escala McCarthy de Aptitudes y Psicomotricidad para Niños (MSCA)", "Batería de Evaluación de niños Kaufman (K.ABC)", "Aptitudes Mentales Primarias (PMA)", "Aptitudes Básicas Generales (ABG-1)", "Aptitudes Básicas Generales 2 (ABG-2)", "Escala Manipulativa Internacional (Leiter-R)", "Escala de Inteligencia No Verbal (TONI-2)", "Woodcock-Johnson III Prueba de Habilidades Cognitivas (WJ-III Cognitivo)", "Test of Cognitive Abilities Woodcock-Johnson III (WJ-III Cognitivo INGLÉS)", "Woodcock-Johnson III Normative Update (WJ-III NU)", "Pruebas de Habilidades Cognitivas Revisada Woodcock-Muñoz (WM-R Cognitivo)", "Cognitive Assessment System (CAS)", "Cognitive Assessment System 2 (CAS 2)", "Delis-Kaplan Executive Function System (D-KEFS)", "Behavior Rating, Inventory of Executive Function (BRIEF)", "Test Factorial de Inteligencia (AMPE-F)", "Inteligencia General Factorial (IGF)", "Test de Inteligencia Creativa (CREA)", "Prueba de Aprovechamiento de Woodcock-Johnson Batería III (WJ-III Aprovechamiento)", "Prueba de Aprovechamiento de Woodcock –Muñoz Revisada (WM-R Aprovechamiento)", "Bracken Basic Concept Scale-Revised (Bracken)", "Kaufman Test of Educational Achievement (K-TEA)", "Prueba del Desarrollo de la Integración Viso Motriz (VMI)", "Koppitz Developmental Scoring System for the Bender Gestalt Test (Koppitz-2)", "Test de Atención d2 (d2)", "Test de Evaluación del Trastorno por Déficit de Atención con Hiperactividad (EDAH)", "Wechsler Memory Scale III (WMS-III)", "Test of Memory and Learning (TOMAL)", "Batería de Evaluación de los Procesos Lectores – Revisada (PROLEC-R)", "Expressive One-Word", "Test de Vocabulario en Imágenes Peabody", "Batería de evaluación de los procesos lectores en alumnos de tercer ciclo de educación y educación secundaria obligatoria (PROLEC-SE)", "Test of Phonological awareness in Spanish (TPAS)", "Cuestionario de 90 síntomas (SCL-90- R)", "Children’s Personality Questionnaire (CPQ)", "Cuestionario Factorial de Personalidad (16 PF-5)", "Inventario Clínico Multiaxial de Millon III (MCMI-III)", "Test de Inteligencia Emocional Mayer-Salovey- Caruso (MSCEIT)", "Escala de adjetivos interpersonales (IAS)", "Inventario diferencial de adjetivos para la evaluación del estado de ánimo (IDDA-EA)", "Cuestionario Big Five (BFQ)", "Minnesota Multiphasic Inventory 2 (MMPI-2- RF)", "Listado de Síntomas Breve (LSB-50)", "Eysenck Personality Questionnaire (EPQ-R)", "Escala de Ansiedad Manifestada en Niños (CMAS-R)", "Cuestionario de Ansiedad Infantil (CAS)", "Test de la Familia", "Test del Árbol", "Test de Apercepción Infantil (CAT-H)", "Test de Patte Noire", "Test de SZONDI", "Test de Apercepción Temática (TAT)", "Draw a person: Screening Procedure for Emotional Disturbance (DAP:SPED)", "Bayley Scale Of Infant Development II edition", "Bayley Scale Of Infant Development - II edition. Motor Scale Test KIT", "Ages &amp; Stages Questionnaires en Español", "Inventario de Desarrollo BATELLE", "Behavioral Inattention Test", "Adaptive Behavior Assessment System II", "Cuestionario de Madurez Neuropsicológica Infantil", "Evaluación Neuropsicológica Breve en Español", "Entrevista para el diagnóstico del Autismo", "Test de Homogeneidad y Preferencia Lateral", "Cuestionario de hábitos y técnicas de estudio", "Instrucciones Complejas", "Monedas: Aptitud de tipo superior (Niveles 1 y 2)", "Comprensión de órdenes escritas Niveles 1, 2, y 3", "Cuestionario de valores personales", "Survey of Interpersonal Values", "Cuestionario de Clima Laboral", "Batería de test para la selección de personal administrativo –I", "Test de aptitudes administrativas -I [a]", "CompeTEA", "Cuestionario de estrés laboral", "Inventario de personalidad para vendedores", "Test de aptitudes administrativas", "Baterías de tareas administrativas", "Temas de educación para la salud", "Diagnóstico Integral de Estudio", "Programa para mejorar la convivencia escolar Programa para mejorar la convivencia escolar", "Programa para mejorar la convivencia escolar", "Programa ABC Dislexia", "Intereses preferencias profesionales", "Acoso y Violencia Escolar","Batería de Socialización 1 y 2", "Batería de Socialización 3"]
	list_test_2 = []
	
	for elem in list_test_1:
		list_test_2.append(SummaryForm.objects.filter(applied_tests__contains=elem).count())
	tuple_test = zip(list_test_1, list_test_2)
	tuple_test_sorted = sorted(tuple_test, key=lambda x: x[1], reverse=True)
	
	
	#----Diagnostico---
	list_diagnosis_1 = ["Discapacidad Intelectual Leve","Discapacidad Intelectual Moderado","Discapacidad Intelectual Grave","Discapacidad Intelectual Profundo","Retraso General del Desarrollo","Trastorno del Lenguaje", "Trastornos Fonológico", "Trastorno de Fluidez (Tartamudeo)", "Autismo","Trastorno Déficit de Atención", "Trastorno Déficit de Atención con Hiperactividad","Dislexia", "Disgrafia", "Discalculia","Trastornos del desarrollo de la coordinación", "Trastornos de Movimientos Estereotipados", "Trastornos de la Tourette", "Trastornos de Tics motores o vocales", "Trastornos de Tic transitorio","Trastorno Esquizotípico de la personalidad", "Trastorno de Delirios", "Trastorno Esquizofreniforme", "Esquizofrenia", "Trastorno Esquizoafectivo", "Trastorno Psicótico inducido por sustancias", "Trastorno Psicótico por afección médica","Trastorno Bipolar  I", "Trastorno Bipolar II", "Trastorno Ciclotímico","Trastorno de Depresión Mayor", "Distimia", "Trastorno Disfórico Premenstrual", "Trastorno de Ansiedad por Separación", "Mutismo Selectivo", "Fobia Específica", "Fobia Social", "Trastorno de Pánico", "Agorafobia","Trastorno de ansiedad generalizada","Trastorno Dismórfico Corporal", "Trastorno de Acumulación", "Tricotilomanía", "Trastorno de excoriación","Trastorno de Apego Reactivo", "Trastorno de relación social desinhibida", "Trastorno de Estrés Postraumático", "Trastorno de Estrés Agudo","Trastorno de ansiedad por enfermedad", "Trastorno Facticio","Pica","Trastorno de rumiación","Trastorno de restricción de ingesta de alimentos", "Anorexia Nerviosa", "Bulimia Nerviosa", "Trastorno por Atracón","Enuresis", "Encopresis","Trastorno de Insomnio", "Trastorno por Hipersomnia", "Narcolepsia","Trastorno negativista desafiante", "Trastorno explosivo intermitente", "Trastorno de personalidad antisocial", "Piromanía", "Cleptomanía","Trastorno por consumo de alcohol", "Trastorno por consumo de cannabis", "Trastorno por consumo de fenciclidina", "Trastorno por sedantes, hipnóticos o ansiolíticos","paranoide", "esquizoide", "esquizotípica", "antisocial", "límite", "histriónica", "narcicistia", "evasiva", "dependiente", "obsesivo-compulsivo","Trastorno de Voyeurismo", "Trastorno de exhibicionismo", "Trastorno de froteurismo", "Trastorno de masoquismo sexual", "Trastorno de sadismo sexual", "Trastorno de pedofilia", "Trastorno de fetichismo","Negligencia","Maltrato","Abuso Sexual","Problemas económicos","Pruebas de Admisión","Problemas Escolares","Habilidad General","Problemas del Habla","Problemas Conductuales","Duelos","Divorcio","Dificultades Familiares","Manejo de Emociones","Relaciones Interpersonales","Trauma","Trastorno Autoinmunológico","Trastornos del Desarrollo","Trastornos Degenerativos","Trastornos por Deficiencias Nutricionales","Trastornos por Toxicidad","Tumores","Accidentes Cerebrovasculares","Anoxia","Epilepsia","Hidrocefalia","Trastornos Infecciosos","Metabólicos","OTROS"]
	
	list_diagnosis_2 = []
	
	for elem in list_diagnosis_1:
		list_diagnosis_2.append(SummaryForm.objects.filter(diagnosis__contains=elem).count())
	tuple_diagnosis = zip(list_diagnosis_1, list_diagnosis_2)
	tuple_diagnosis_sorted = sorted(tuple_diagnosis, key=lambda x: x[1], reverse=True)
	
	params = {'tuple_gender' : tuple_gender, 'tuple_age' : tuple_age, 'tuple_education' : tuple_education, 'tuple_status' : tuple_status, 'tuple_service' : tuple_service, 'tuple_referred':tuple_referred, 'tuple_consultation_sorted':tuple_consultation_sorted, 'tuple_test_sorted':tuple_test_sorted, 'tuple_diagnosis_sorted':tuple_diagnosis_sorted}
	return render(request,'sharedarea/record_statistics.html', params)

def record(request,r,r_id):
	my_user = request.user
	if (not my_user.is_authenticated()):
		return redirect('/')
		
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')	
		
	mensaje = ""
	if request.method == 'POST':
		form = recordForm(request.POST, instance=my_record)
		if form.is_valid():
			form.save()
			mensaje = "Cambios realizados con éxito"
	else:
		form = recordForm(instance=my_record)
	params = {'id_record' : r_id, 'identifier_record' : r, 'record_form' : form, 'mensaje' : mensaje}
	return render(request,'sharedarea/record.html', params)
    

def record_dashboard(request):
	if (not request.user.is_authenticated()):
		return redirect('/')
		
	if request.method == 'POST':
		records = []
		showflag1=showflag2=showflag3=showflag4=showflag5=showflag6=showflag7= False;
		
		show1 = request.POST.get("limit_radio_1")
		if(not show1==None):
			show1="Psicoterapia"
			showflag1 = True
		else:
			show1=""
		show2 = request.POST.get("limit_radio_2")
		if(not show2==None):
			show2="Consejería"
			showflag2 = True
		else:
			show2=""
		show3 = request.POST.get("limit_radio_3")
		if(not show3==None):
			show3="Evaluación Psicológica"
			showflag3 = True
		else:
			show3=""
		show4 = request.POST.get("limit_radio_4")
		if(not show4==None):
			show4="Evaluación Psicoeducativa"
			showflag4 = True
		else:
			show4=""
		show5 = request.POST.get("limit_radio_5")
		if(not show5==None):
			show5=None
			showflag5 = True
		else:
			show5=""
		show6 = request.POST.get("limit_radio_6")
		if(not show6==None):
			show6=None
			showflag6 = True
		else:
			show6=0
		show7 = request.POST.get("limit_radio_7")
		if(not show7==None):
			show7=None
			showflag7 = True
		else:
			show7=0
		
		if request.user.groups.filter(name='Administrador').exists():
			records = Record.objects.select_related("client_id_client").select_related("student").select_related("professor").filter(Q(record_type=show1)|Q(record_type=show2)|Q(record_type=show3)|Q(record_type=show4)|Q(record_type=show5)|Q(professor_id=show6)|Q(student_id=show7))
		elif request.user.groups.filter(name='Catedrático').exists():
			records = Record.objects.select_related("client_id_client").select_related("student").select_related("professor").filter(Q(professor_id=request.user.id)&(Q(record_type=show1)|Q(record_type=show2)|Q(record_type=show3)|Q(record_type=show4)|Q(record_type=show5)|Q(professor_id=show6)|Q(student_id=show7)))
		elif request.user.groups.filter(name='Estudiante').exists():
			records = Record.objects.select_related("client_id_client").select_related("student").select_related("professor").filter(Q(student_id=request.user.id)&(Q(record_type=show1)|Q(record_type=show2)|Q(record_type=show3)|Q(record_type=show4)|Q(record_type=show5)|Q(professor_id=show6)|Q(student_id=show7)))
			
		palabra_clave = request.POST.get("key_word")
		order = request.POST.get("order_radio")
		order_flag = 0
		if(order=="catedratico"):
			order="professor_id__last_name"
			order_flag = 2
		elif(order=="paciente"):
			order="client_id_client__name"
			order_flag = 1
		elif(order=="estudiante"):
			order="student_id__last_name"
			order_flag = 3
		elif(order=="fecha_desc"):
			order="-record_date"
			order_flag = 4
		elif(order=="fecha_asc"):
			order="record_date"
			order_flag = 5
		
		
		"""
		show1 = request.POST.get("limit_radio_1")
		if(not show1==None):
			show1="Psicoterapia"
			showflag1 = True
		show2 = request.POST.get("limit_radio_2")
		if(not show2==None):
			show2="Consejería"
			showflag2 = True
		show3 = request.POST.get("limit_radio_3")
		if(not show3==None):
			show3="Evaluación Psicológica"
			showflag3 = True
		show4 = request.POST.get("limit_radio_4")
		if(not show4==None):
			show4="Evaluación Psicoeducativa"
			showflag4 = True
		show5 = request.POST.get("limit_radio_5")
		if(not show5==None):
			show5="None"
			showflag5 = True
		show6 = request.POST.get("limit_radio_6")
		if(not show6==None):
			show6="None"
			showflag6 = True
		show7 = request.POST.get("limit_radio_7")
		if(not show7==None):
			show7="None"
			showflag7 = True
		"""
		if(not palabra_clave == ""):
			records = records.filter(Q(client_id_client__name__contains=palabra_clave) | Q(professor_id__first_name__contains=palabra_clave) | Q(professor_id__last_name__contains=palabra_clave) | Q(student_id__first_name__contains=palabra_clave) | Q(student_id__last_name__contains=palabra_clave))
		"""
		if(not show1==None):
			records = records.exclude(record_type=show1)
		if(not show2==None):
			records = records.exclude(record_type=show2)
		if(not show3==None):
			records = records.exclude(record_type=show3)
		if(not show4==None):
			records = records.exclude(record_type=show4)
		if(not show5==None):
			records = records.exclude(record_type=None)
		if(not show6==None):
			records = records.exclude(professor_id=None)
		if(not show7==None):
			records = records.exclude(student_id=None)
		"""
		if(not order==None):
			records = records.order_by(order)
		params = {'records':records, 'palabra':palabra_clave, 'flag1':showflag1, 'flag2':showflag2, 'flag3':showflag3, 'flag4':showflag4, 'flag5':showflag5, 'flag6':showflag6, 'flag7':showflag7, 'order':order_flag}
		return render(request,'sharedarea/record_dashboard.html',params)
		
		
	if request.user.groups.filter(name='Administrador').exists():
		records = Record.objects.select_related("client_id_client").select_related("student").select_related("professor").all().order_by("-record_date")
	elif request.user.groups.filter(name='Catedrático').exists():
		records = Record.objects.select_related("client_id_client").select_related("student").select_related("professor").filter(professor_id=request.user.id).order_by("-record_date")
	elif request.user.groups.filter(name='Estudiante').exists():
		records = Record.objects.select_related("client_id_client").select_related("student").select_related("professor").filter(student_id=request.user.id).order_by("-record_date")
	else:
		records = []
	params = {'records':records, 'flag1':True, 'flag2':True, 'flag3':True, 'flag4':True, 'flag5':True, 'flag6':True, 'flag7':True}
	return render(request,'sharedarea/record_dashboard.html',params)

def file_view(request,r,r_id,f_id,f_name):
	if (not request.user.is_authenticated()):
		return redirect('/')
	#Verificar permiso
	my_user = request.user
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')	
	
	pdf = UploadForm.objects.get(id_upload_form=f_id)
	pdf_data = open(settings.PRIVATE_RECORD_ROOT+pdf.link, "rb").read()
	mime = MimeTypes()
	url = urllib.pathname2url(settings.PRIVATE_RECORD_ROOT+pdf.link)
	mime_type = mime.guess_type(url)
	return HttpResponse(pdf_data, content_type=mime_type)
	
def picture_view(request,field_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
	#Verificar permiso
	
	my_user = request.user
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	
	field = FormHasField.objects.get(id_form_has_field = field_id)
	image_data = open(settings.PRIVATE_RECORD_ROOT+field.text_answer, "rb").read()

	mime = MimeTypes()
	url = urllib.pathname2url(settings.PRIVATE_RECORD_ROOT+field.text_answer)
	mime_type = mime.guess_type(url)
	return HttpResponse(image_data, content_type=mime_type)

def record_view(request,r,r_id,f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
	#Agregar valdacion de permisos
	my_record = Record.objects.filter(id_record=r)
	
	my_user = request.user
	my_record_2 = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record_2.student_id == None and my_record_2.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record_2.student_id == None):
		if not (my_user.id == my_record_2.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record_2.professor == None):
		if not (my_user.id == my_record_2.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record_2.student_id or my_user.id == my_record_2.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	
	if(f_id=='0'):
		my_form_type = FormType.objects.get(id_form_type=1)
		form_to_display = Form.objects.select_related("form_type_id_form_type").get(record_id_record = my_record, form_type_id_form_type = my_form_type)
	else:
		form_to_display = Form.objects.select_related("form_type_id_form_type").get(id_form=f_id)
		
	forms = Form.objects.select_related("form_type_id_form_type").filter(record_id_record=my_record)
	files = UploadForm.objects.select_related("form_type_id_form_type").filter(record_id_record=my_record)
	summary = SummaryForm.objects.select_related("form_type_id_form_type").filter(record_id_record=my_record)
	forms_ids = Form.objects.select_related("form_type_id_form_type").filter(record_id_record=my_record, form_type_id_form_type__multiple=0).values('form_type_id_form_type__id_form_type')
	files_ids = UploadForm.objects.select_related("form_type_id_form_type").filter(record_id_record=my_record, form_type_id_form_type__multiple=0).values('form_type_id_form_type__id_form_type')
	summary_ids = SummaryForm.objects.select_related("form_type_id_form_type").filter(record_id_record=my_record, form_type_id_form_type__multiple=0).values('form_type_id_form_type__id_form_type')
	forms_missing = FormType.objects.exclude(id_form_type__in = forms_ids).exclude(id_form_type__in = files_ids).exclude(id_form_type__in = summary_ids)

	answers = FormHasField.objects.select_related("field_id_field").filter(form_id_form=form_to_display).order_by('field_id_field_id__field_number') #se cambio all por filter
	#table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display).order_by('form_table_id_form_table_id__field_number')
	form_fields = FormTable.objects.filter(form_type_id_form_type = form_to_display.form_type_id_form_type).order_by('field_number');
	both_answers = list(answers) + list(form_fields)
	#answers_sorted = sorted(both_answers,key=lambda x: x.field_id_field.field_number if hasattr(x, 'field_id_field') else x.form_table_id_form_table.field_number, reverse=False)
	answers_sorted = sorted(both_answers,key=lambda x: x.field_id_field.field_number if hasattr(x, 'field_id_field') else x.field_number, reverse=False)
	
	extra = []
	for temp_answer in answers_sorted:
		try:
			temp_answer.field_type == 7
			extra.append(FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display,form_table_id_form_table = temp_answer.id_form_table))
		except AttributeError:
			extra.append("")
            
	my_tuple = zip(answers_sorted,extra)
	
	comentarios = Comments.objects.filter(form_id_form=form_to_display)
	comentarios = comentarios.extra(order_by = ['id_comments'])
	tupla_comentarios = []
	
	for comentario in comentarios:
		user = comentario.auth_user.first_name+" "+comentario.auth_user.last_name
		
		usuario= get_object_or_404(AuthUser, pk=comentario.auth_user.pk)
		
		tupla = {"nombre":user,"message":comentario.message,"fecha":comentario.date_comment,"formUser":usuario}
		tupla_comentarios.append(tupla)
	
	miusuario= get_object_or_404(AuthUser, pk=request.user.pk)
	params = {'id_record' : r_id, 'identifier_record' : r, 'answer_fields' : answers_sorted, 'forms_added' : forms, 'files_added': files, 'summary_added':summary, 'forms_missing' : forms_missing, 'form_displaying' : form_to_display,"comentarios":tupla_comentarios, 'answers_tuple' : my_tuple, 'miusuario':miusuario}
	return render(request,'sharedarea/record_manager.html',params)

def add_comment(request,r,r_id,f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
	comentario_text = request.POST.get('mi-comentario','')
	#Agregar valdacion de permisos
	my_record = Record.objects.filter(id_record=r)
	if(f_id=='0'):
		my_form_type = FormType.objects.get(id_form_type=1)
		form_to_display = Form.objects.select_related("form_type_id_form_type").get(record_id_record = my_record, form_type_id_form_type = my_form_type)
	else:
		form_to_display = Form.objects.select_related("form_type_id_form_type").get(id_form=f_id)
	user = AuthUser.objects.filter(username = request.user.username)[0]
	c = Comments(message=comentario_text,auth_user=user,form_id_form=form_to_display)
	c.save()
	return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/'+str(f_id))

def form_add(request,r,r_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
	#Agregar validacion de permisos
	
	my_user = request.user
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	
	if request.method == 'POST':
		my_type = request.POST.get("form_identifier")
		if(my_type == None):
			return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/0')
		
		#Validar disponibilidad
		my_form_type = FormType.objects.get(id_form_type=my_type)
		
		
		if(my_form_type.is_file==1):
			form = fileUploadForm2()
			params = {'id_record' : r_id, 'identifier_record' : r, 'my_form_type':my_form_type, 'form': form}
			return render(request,'sharedarea/record_file_upload.html',params)
		elif(my_form_type.is_file==2):
			form = summaryForm()
			params = {'id_record' : r_id, 'identifier_record' : r, 'my_form_type':my_form_type, 'form': form}
			return render(request,'sharedarea/record_investigation.html',params)
		else:
			fields = Field.objects.filter(form_type_id_form_type = my_form_type).order_by('field_number');
			form_fields = FormTable.objects.filter(form_type_id_form_type = my_form_type).order_by('field_number');
			both_fields = list(fields) + list(form_fields)
			fields_sorted = sorted(both_fields, key=lambda x: x.field_number, reverse=False)
			params = {'id_record' : r_id, 'identifier_record' : r, 'record_fields' : fields_sorted, 'my_form_type':my_form_type}
			return render(request,'sharedarea/record_add.html',params)
	return redirect('/')

def add_summary(request,r,r_id,f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
	
	my_user = request.user
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	
	if request.method == 'POST':
		form = summaryForm(request.POST)
		
		my_form_type = FormType.objects.get(id_form_type=f_id)
		
		#----verificar duplicado
		if(not my_form_type.multiple):
			if(SummaryForm.objects.filter(form_type_id_form_type = my_form_type,record_id_record = my_record).exists()):
				return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/0')
			
		if form.is_valid():
			my_record = Record.objects.get(id_record=r)
			
			my_summary_form = SummaryForm()
			my_summary_form.gender = form.cleaned_data['gender']
			my_summary_form.birth_date = form.cleaned_data['birth_date']
			my_summary_form.age = form.cleaned_data['age']
			my_summary_form.education = form.cleaned_data['education']
			my_summary_form.registration_date = form.cleaned_data['registration_date']
			my_summary_form.termination_date = form.cleaned_data['termination_date']
			my_summary_form.current_status = form.cleaned_data['current_status']
			my_summary_form.service_type = form.cleaned_data['service_type']
			my_summary_form.consultation_reason = form.cleaned_data['consultation_reason']
			my_summary_form.applied_tests = form.cleaned_data['applied_tests']
			my_summary_form.number_sessions = form.cleaned_data['number_sessions']
			my_summary_form.diagnosis = form.cleaned_data['diagnosis']
			my_summary_form.referred_by =form.cleaned_data['referred_by']
			my_summary_form.record_id_record = my_record
			my_summary_form.form_type_id_form_type = my_form_type
			my_summary_form.save()
			return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/0')
		else:
			params = {'id_record' : r_id, 'identifier_record' : r, 'my_form_type':my_form_type, 'form': form}
			return render(request,'sharedarea/record_investigation.html',params)
	else:
		return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/0')

def add_file(request,r,r_id,f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
		
	my_user = request.user
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')	
	
	if request.method == 'POST':
		form = fileUploadForm2(request.POST, request.FILES)
		
		my_form_type = FormType.objects.get(id_form_type=f_id)
		my_record = Record.objects.get(id_record=r)
		
		#----verificar duplicado
		if(not my_form_type.multiple):
			if(UploadForm.objects.filter(form_type_id_form_type = my_form_type,record_id_record = my_record).exists()):
				return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/0')
		
		if form.is_valid():
			
			f_upload = request.FILES['file_to_upload']
			#algo = f_upload.read()
			algo2 = ''
			for chunk in f_upload.chunks():
				algo2 = algo2+chunk
			path = default_storage.save(f_upload.name, ContentFile(algo2))
			try:
				os.makedirs(settings.PRIVATE_RECORD_ROOT + "/"+ r_id +"/" + my_form_type.code + "/")
				int('2')
			except OSError as e:
				if e.errno == 17:
				    pass
			algo = settings.PRIVATE_RECORD_ROOT + "/"+ r_id +"/" + my_form_type.code +"/"+ path
			os.rename(settings.MEDIA_ROOT + "/" + path, settings.PRIVATE_RECORD_ROOT + "/"+ r_id +"/" + my_form_type.code +"/"+ path)
			
			my_file_to_upload = UploadForm()
			my_file_to_upload.link = "/"+ r_id +"/" + my_form_type.code +"/"+ path
			my_file_to_upload.record_id_record = my_record
			my_file_to_upload.form_type_id_form_type = my_form_type
			if(my_form_type.multiple):
				my_file_to_upload.name = form.cleaned_data['name_of_file']
			my_file_to_upload.save()
			return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/0')
		else:
			params = {'id_record' : r_id, 'identifier_record' : r, 'my_form_type':my_form_type, 'form': form}
			return render(request,'sharedarea/record_file_upload.html',params)
	return redirect('/')

def remove_file(request,r,r_id):
	
	if (not request.user.is_authenticated()):
		return redirect('/')
		
	my_user = request.user
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	
	if request.method == 'POST':
		my_type = request.POST.get("file_identifier")
		if(my_type == None):
			return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/0')
		
		#Validar disponibilidad
		my_file = UploadForm.objects.get(id_upload_form=my_type)
		my_url = settings.PRIVATE_RECORD_ROOT + my_file.link
		try:
			os.remove(my_url)
			my_file.delete()
		except OSError as e:
			pass
		return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/0')

def save_form(request,r,r_id,f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
		
	my_user = request.user
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	
	if request.method == 'POST':
		#Verificar de nuevo no se guarde uno que no se debe
		
		my_form_type = FormType.objects.get(id_form_type=f_id)
		my_record = Record.objects.get(id_record=r)
		
		if(not my_form_type.multiple):
			if(Form.objects.filter(form_type_id_form_type = my_form_type,record_id_record = my_record).exists()):
				return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/0')
		
		#Obtener campos del formato
		my_fields = Field.objects.filter(form_type_id_form_type = f_id)
		
		my_form_type = FormType.objects.get(id_form_type=f_id)
		
		my_table_fields = FormTable.objects.filter(form_type_id_form_type = f_id).order_by('field_number')
		my_both_fields = list(my_fields) + list(my_table_fields)
		my_fields_sorted = sorted(my_both_fields, key=lambda x: x.field_number, reverse=False)
		
		#Listas para guardar contenido y errores
		my_errors = []
		my_contents = []
		error = False
		
		num_filas_tabla = {2:6, 6:12, 7:4, 8:24, 9:28, 10:30, 11:45, 12:9, 13:16, 15:8, 16:20, 19:11, 21:8}
		
		#Recorrer campos
		for my_field in my_fields_sorted:
			#verificar numero
			if(my_field.field_type == 2):
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				try:
					my_temp_val = int(content)
					my_errors.append("")
				except ValueError:
					error = True
					my_errors.append("Debe ingresar un número")
			elif(my_field.field_type == 4):
				content = request.POST.get(my_field.field_identifier)
				try:
					temp_date = datetime.strptime(content, "%d/%m/%Y")
					my_contents.append(temp_date.strftime("%d/%m/%Y"))
					my_errors.append("")
				except ValueError:
					error = True
					my_contents.append(content)
					my_errors.append("Debe ingresar una fecha con forma dd/mm/aaaa")
			elif(my_field.field_type == 12):
				try:
					my_image_to_upload = request.FILES[my_field.field_identifier]
					try:
						img = Image.open(my_image_to_upload)
						img.verify()
						my_contents.append("")
						my_errors.append("")
					except IOError:
						error = True
						my_contents.append("")
						my_errors.append("Debe subir una imagen")
				except MultiValueDictKeyError:
					my_contents.append("")
					my_errors.append("")
			elif(my_field.field_type == 7):
				num_col = my_field.number_columns
				num_fil = num_filas_tabla[my_field.id_form_table]
				name_table = my_field.form_table_identifier
				temp_table = []
				for x in range(1,num_fil+1):
					row = []
					for y in range(1, num_col+1):
						row.append(request.POST.get(name_table+"_col_"+str(x)+"_"+str(y)))
					temp_table.append(row)
				my_contents.append(temp_table)
				my_errors.append("")
				
			elif(my_field.field_type == 9):
				name_table = my_field.form_table_identifier
				temp_table = []
				num_col = my_field.number_columns
				num_fil = int(request.POST.get("filas_"+name_table))
				for x in range(1,num_fil+1):
					row = []
					for y in range(1, num_col+1):
						celda = request.POST.get(name_table+"_col_"+str(x)+"_"+str(y))
						if(celda == None):
							celda = ""
							row.append(celda)
						else:
							row.append(celda)
					temp_table.append(row)
				my_contents.append(temp_table)
				my_errors.append("")
			else:
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				my_errors.append("")
				
		#Hubo fallo y se mostraran errores
		if(error):
			my_tuple = zip(my_fields_sorted,my_contents,my_errors)	
			params = {'id_record' : r_id, 'identifier_record' : r, 'answer_tuple' : my_tuple, 'my_form_type':my_form_type}	
			return render(request,'sharedarea/record_add_2.html',params)
		
		#Encontrar expediente y tipo formato
		my_record = Record.objects.get(id_record=r)
		my_form_type = FormType.objects.get(id_form_type = f_id)
		
		#Crear Form
		my_form = Form()
		my_form.record_id_record = my_record
		my_form.form_type_id_form_type = my_form_type
		my_form.save()

		#Recorrer y guardar los campos
		for my_field in my_fields:
			if(not my_field.field_type == 12):
				content = request.POST.get(my_field.field_identifier)
			else:
				my_image_to_upload = request.FILES[my_field.field_identifier]
			my_insert = FormHasField()
			my_insert.form_id_form = my_form
			my_insert.field_id_field = my_field
			if(my_field.field_type == 1):
				my_insert.text_answer = content
			if(my_field.field_type == 2):
				my_insert.int_answer = content
			if(my_field.field_type == 4):
				temp_date = datetime.strptime(content, "%d/%m/%Y")
				my_insert.date_answer = temp_date.strftime("%Y-%m-%d")
			if(my_field.field_type == 5):
				if(content==None):
					my_insert.text_answer = ""
				else:
					my_insert.text_answer = content
			if(my_field.field_type == 6):
				my_insert.text_answer = content
			if(my_field.field_type == 11):
				my_insert.text_answer = content
			if(my_field.field_type == 12):
				algo2 = ''
				for chunk in my_image_to_upload.chunks():
					algo2 = algo2+chunk
				path = default_storage.save(my_image_to_upload.name, ContentFile(algo2))
				try:
					os.makedirs(settings.PRIVATE_RECORD_ROOT + "/"+ r_id +"/" + 'genograma' + "/")
				except OSError as e:
					if e.errno == 17:
						pass
				os.rename(settings.MEDIA_ROOT + "/" + path, settings.PRIVATE_RECORD_ROOT + "/"+ r_id +"/" + 'genograma' +"/"+ path)
				
				my_insert.text_answer = "/"+ r_id +"/" + 'genograma' +"/"+ path
			my_insert.save()
		for my_table_field in my_table_fields:
			if(my_table_field.field_type == 7):
				num_col = my_table_field.number_columns
				num_fil = num_filas_tabla[my_table_field.id_form_table]
				name_table = my_table_field.form_table_identifier
				for x in range(1,num_fil+1):
					my_insert2 = FormHasFormTable()
					my_insert2.form_id_form = my_form
					my_insert2.form_table_id_form_table = FormTable.objects.get(form_table_identifier = name_table)
					if(num_col>=1):
						content1 = request.POST.get(name_table+"_col_"+str(x)+"_1")
						my_insert2.answer_col_1 = content1
					if(num_col>=2):
						content2 = request.POST.get(name_table+"_col_"+str(x)+"_2")
						my_insert2.answer_col_2 = content2
					if(num_col>=3):
						content3 = request.POST.get(name_table+"_col_"+str(x)+"_3")
						my_insert2.answer_col_3 = content3
					if(num_col>=4):
						content4 = request.POST.get(name_table+"_col_"+str(x)+"_4")
						my_insert2.answer_col_4 = content4
					if(num_col>=5):
						content5 = request.POST.get(name_table+"_col_"+str(x)+"_5")
						my_insert2.answer_col_5 = content5
					if(num_col>=6):
						content6 = request.POST.get(name_table+"_col_"+str(x)+"_6")
						my_insert2.answer_col_6 = content6
					if(num_col>=7):
						content7 = request.POST.get(name_table+"_col_"+str(x)+"_7")
						my_insert2.answer_col_7 = content7
					my_insert2.save()
			else:
				name_table = my_table_field.form_table_identifier
				num_col = my_table_field.number_columns
				num_fil = int(request.POST.get("filas_"+name_table))
				for x in range(1,num_fil+1):
					my_insert2 = FormHasFormTable()
					my_insert2.form_id_form = my_form
					my_insert2.form_table_id_form_table = FormTable.objects.get(form_table_identifier = name_table)
					
					content1 = content2 = content3 = content4 = content5 = content6 =  content7 = ""
					if(num_col>=1):
						content1 = request.POST.get(name_table+"_col_"+str(x)+"_1")
						if(content1 == None):
							content1 = ""
						my_insert2.answer_col_1 = content1
					if(num_col>=2):
						content2 = request.POST.get(name_table+"_col_"+str(x)+"_2")
						if(content2 == None):
							content2 = ""
						my_insert2.answer_col_2 = content2
					if(num_col>=3):
						content3 = request.POST.get(name_table+"_col_"+str(x)+"_3")
						if(content3 == None):
							content3 = ""
						my_insert2.answer_col_3 = content3
					if(num_col>=4):
						content4 = request.POST.get(name_table+"_col_"+str(x)+"_4")
						if(content4 == None):
							content4 = ""
						my_insert2.answer_col_4 = content4
					if(num_col>=5):
						content5 = request.POST.get(name_table+"_col_"+str(x)+"_5")
						if(content5 == None):
							content5 = ""
						my_insert2.answer_col_5 = content5
					if(num_col>=6):
						content6 = request.POST.get(name_table+"_col_"+str(x)+"_6")
						if(content6 == None):
							content6 = ""
						my_insert2.answer_col_6 = content6
					if(num_col>=7):
						content7 = request.POST.get(name_table+"_col_"+str(x)+"_7")
						if(content7 == None):
							content7 = ""
						my_insert2.answer_col_7 = content7
					if(not(content1==content2==content3==content4==content5==content6==content7=="")):
						my_insert2.save()
			
		
		#fields = Field.objects.all().order_by('field_number');
		#form_fields = FormTable.objects.all().order_by('field_number');
		#both_fields = list(fields) + list(form_fields)
		#fields_sorted = sorted(both_fields, key=lambda x: x.field_number, reverse=False)
		#params = {'id_record' : r_id, 'record_fields' : fields_sorted}
		return redirect('/record_view/'+str(r)+'/'+str(r_id)+'/'+str(my_form.id_form))

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def new_record(request):
	if (not request.user.is_authenticated()):
		return redirect('/')
		
	#En caso se deba crear y guardar
	if request.method == 'POST':
		#------Verificar todos los campos --------
		my_fields = Field.objects.filter(form_type_id_form_type = 1).order_by('field_number')
		my_table_fields = FormTable.objects.filter(form_type_id_form_type = 1).order_by('field_number')
		my_both_fields = list(my_fields) + list(my_table_fields)
		my_fields_sorted = sorted(my_both_fields, key=lambda x: x.field_number, reverse=False)
		#Recorrer campos
		my_errors = []
		my_contents = []
		error = False
		for my_field in my_fields_sorted:
			#verificar numero
			if(my_field.field_type == 2):
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				try:
					my_temp_val = int(content)
					my_errors.append("")
				except ValueError:
					error = True
					my_errors.append("Debe ingresar un número")
			elif(my_field.field_type == 4):
				content = request.POST.get(my_field.field_identifier)
				try:
					temp_date = datetime.strptime(content, "%d/%m/%Y")
					my_contents.append(temp_date.strftime("%d/%m/%Y"))
					my_errors.append("")
				except ValueError:
					error = True
					my_contents.append(content)
					my_errors.append("Debe ingresar una fecha con forma dd/mm/aaaa")
			elif(my_field.field_type == 7):
				schedule_table = []
				dias = ["lunes","martes", "miercoles", "jueves", "viernes", "sabado"]
				for x in range(1,7):
					row = []
					row.append(dias[x-1])
					row.append(request.POST.get("am_"+str(x)))
					row.append(request.POST.get("pm_"+str(x)))
					schedule_table.append(row)
				my_contents.append(schedule_table)
				my_errors.append("")
			else:
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				my_errors.append("")
				
		#Hubo fallo y se mostraran errores
		if(error):
			my_tuple = zip(my_fields_sorted,my_contents,my_errors)	
			params = {'answer_tuple' : my_tuple}	
			return render(request,'sharedarea/record_create_2.html',params)
					
		#------Si no hay problema crear y guardar nuevo expediente-----
		#Crear nuevos objetos
		my_record = Record()
		my_client = Client()
		my_form = Form()
		
		
		#Crear Cliente
		my_client.name = request.POST.get("nombre_cliente")
		#my_client.last_name = 
		my_client.telephone = request.POST.get("telefono")
		my_client.address = request.POST.get("direccion")
		my_client.email = request.POST.get("correo")
		
		#Crear usuario para cliente si es necesario
		if request.POST.get('userRadio') == 'yes':
			user_name = id_generator()
			while User.objects.filter(username=user_name).exists():
				user_name = id_generator()
			user_pass = id_generator()
			my_user = User.objects.create_user(user_name, my_client.email, user_pass)
			my_user.first_name = my_client.name
			my_group = Group.objects.get(name='Cliente')
			my_user.groups.add(my_group)
			my_user.save()
			#Enviar correo
			email = EmailMessage('Sus datos de autenticación', ' usuario: '+user_name+"\n contraseña: "+user_pass+"\n \n Este es un mensaje automático, por favor no responder a él.", to=[my_client.email])
			email.send()
			
			my_user_2 = AuthUser.objects.get(id=my_user.id)
			my_client.client_user = my_user_2
		
		my_client.save()

		
		#Crear Record
		my_record.client_id_client = my_client
		my_record.record_type = request.POST.get("servicio_cipa")
		my_temp_date = request.POST.get("fecha_hoy")
		my_temp_date_2 = datetime.strptime(my_temp_date, "%d/%m/%Y")
		my_record.record_date = my_temp_date_2.strftime("%Y-%m-%d")
		my_record.save()
		
		#Crear Form
		my_form.record_id_record = my_record
		my_form.form_type_id_form_type = FormType.objects.get(id_form_type = 1)
		my_form.save()	
		
		#Recorrer campos
		for my_field in my_fields:
			content = request.POST.get(my_field.field_identifier)
			#Crear campos
			my_insert = FormHasField()
			my_insert.form_id_form = my_form
			my_insert.field_id_field = my_field
			if(my_field.field_type == 1):
				my_insert.text_answer = content			
			if(my_field.field_type == 2):
				my_insert.int_answer = content
			if(my_field.field_type == 4):
				temp_date = datetime.strptime(content, "%d/%m/%Y")
				my_insert.date_answer = temp_date.strftime("%Y-%m-%d")
			if(my_field.field_type == 5):
				if(content==None):
					my_insert.text_answer = ""
				else:
					my_insert.text_answer = content
			if(my_field.field_type == 6):
				my_insert.text_answer = content
			my_insert.save()
			
		for x in range(1,7):
			content1 = request.POST.get("am_"+str(x))
			content2 = request.POST.get("pm_"+str(x))
			my_insert2 = FormHasFormTable()
			my_insert2.form_id_form = my_form
			my_insert2.form_table_id_form_table = FormTable.objects.get(form_table_identifier = "horario_table")
			my_insert2.answer_col_1 = content1
			my_insert2.answer_col_2 = content2
			my_insert2.save()
		return redirect('/calendario')	
		
					
	fields = Field.objects.filter(form_type_id_form_type = 1).order_by('field_number'); 
	form_fields = FormTable.objects.filter(form_type_id_form_type = 1).order_by('field_number');
	both_fields = list(fields) + list(form_fields)
	fields_sorted = sorted(both_fields, key=lambda x: x.field_number, reverse=False)
	params = {'record_fields' : fields_sorted}
	return render(request,'sharedarea/record_create.html',params)


def record_edit(request,r,r_id,f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
		
	my_user = request.user
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
    
	#En caso se deba guardar
	if request.method == 'POST':
		#----------Verificar todos los campos-----------
		num_filas_tabla = {2:6, 6:12, 7:4, 8:24, 9:28, 10:30, 11:45, 12:9, 13:16, 15:8, 16:20, 19:11, 21:8}
		
		#Obtener los campos del formato (campos y tablas en orden)
		my_form = Form.objects.get(id_form=f_id)
		my_fields = Field.objects.filter(form_type_id_form_type = my_form.form_type_id_form_type).order_by('field_number')
		my_table_fields = FormTable.objects.filter(form_type_id_form_type = my_form.form_type_id_form_type).order_by('field_number')
		my_both_fields = list(my_fields) + list(my_table_fields)
		my_fields_sorted = sorted(my_both_fields, key=lambda x: x.field_number, reverse=False)
		#Recorrer campos
		my_errors = []
		my_contents = []
		error = False
		for my_field in my_fields_sorted:
		#verificar numero
			if(my_field.field_type == 2):
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				try:
					my_temp_val = int(content)
					my_errors.append("")
				except ValueError:
					error = True
					my_errors.append("Debe ingresar un número")
			elif(my_field.field_type == 4):
				content = request.POST.get(my_field.field_identifier)
				
				try:
					temp_date = datetime.strptime(content, "%d/%m/%Y")
					my_contents.append(temp_date.strftime("%d/%m/%Y"))
					my_errors.append("")
					#temp_date=parse_date(content)
					#if(temp_date==None):
					#	error = True
					#	int("")
					#	my_errors.append("Debe ingresar una fecha con forma dd-mm-aaaa")
					#else:
					#	my_errors.append("")
				except ValueError:
					error = True
					my_contents.append(content)
					my_errors.append("Debe ingresar una fecha con forma dd-mm-aaaa")
			elif(my_field.field_type == 12):
				try:
					my_image_to_upload = request.FILES[my_field.field_identifier]
					try:
						img = Image.open(my_image_to_upload)
						img.verify()
						my_contents.append("")
						my_errors.append("")
					except IOError:
						error = True
						my_contents.append("")
						my_errors.append("Debe subir una imagen")
				except MultiValueDictKeyError:
					my_contents.append("")
					my_errors.append("")
			elif(my_field.field_type == 7):
				num_col = my_field.number_columns
				num_fil = num_filas_tabla[my_field.id_form_table]
				name_table = my_field.form_table_identifier
				temp_table = []
				for x in range(1,num_fil+1):
					row = []
					for y in range(1, num_col+1):
						row.append(request.POST.get(name_table+"_col_"+str(x)+"_"+str(y)))
					temp_table.append(row)
				my_contents.append(temp_table)
				my_errors.append("")
			elif(my_field.field_type == 9):
				name_table = my_field.form_table_identifier
				temp_table = []
				num_col = my_field.number_columns
				num_fil = int(request.POST.get("filas_"+name_table))
				for x in range(1,num_fil+1):
					row = []
					for y in range(1, num_col+1):
						celda = request.POST.get(name_table+"_col_"+str(x)+"_"+str(y))
						if(celda == None):
							celda = ""
							row.append(celda)
						else:
							row.append(celda)
						
					temp_table.append(row)
				my_contents.append(temp_table)
				my_errors.append("")
			else:
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				my_errors.append("")
		
		#Hubo fallo y se mostraran errores
		if(error):
			form_to_display = Form.objects.select_related("form_type_id_form_type").get(id_form=f_id)
			my_tuple = zip(my_fields_sorted,my_contents,my_errors)	
			params = {'id_record' : r_id, 'identifier_record' : r, 'answer_tuple' : my_tuple, 'form_displaying' : form_to_display}	
			return render(request,'sharedarea/record_edit_2.html',params)		
		#Actualizar campos
		form_to_display = Form.objects.select_related("form_type_id_form_type").get(id_form=f_id)
		answers = FormHasField.objects.select_related("field_id_field").filter(form_id_form=form_to_display)
		table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display)
		for answer in answers:
			if(answer.field_id_field.field_type==1):
				answer.text_answer = request.POST.get(answer.field_id_field.field_identifier)
				answer.save()
			elif(answer.field_id_field.field_type==2):
				answer.int_answer = request.POST.get(answer.field_id_field.field_identifier)
				answer.save()
			elif(answer.field_id_field.field_type==4):
				content = request.POST.get(answer.field_id_field.field_identifier)
				temp_date = datetime.strptime(content, "%d/%m/%Y")
				answer.date_answer = temp_date.strftime("%Y-%m-%d")
				answer.save()
			elif(answer.field_id_field.field_type==5):
				content = request.POST.get(answer.field_id_field.field_identifier)
				if(content==None):
					answer.text_answer = ""
				else:
					answer.text_answer = content
				answer.save()
			elif(answer.field_id_field.field_type==6):
				answer.text_answer = request.POST.get(answer.field_id_field.field_identifier)
				answer.save()
			elif(answer.field_id_field.field_type==11):
				answer.text_answer = request.POST.get(answer.field_id_field.field_identifier)
				answer.save()
			elif(answer.field_id_field.field_type==12):
				is_file = True
				try:
					my_image_to_upload = request.FILES[answer.field_id_field.field_identifier]
				except MultiValueDictKeyError:
					is_file = False
				
				if(is_file):
					temp_url = settings.PRIVATE_RECORD_ROOT + answer.text_answer
					try:
						os.remove(temp_url)
					except OSError as e:
						pass
				
					algo2 = ''
					for chunk in my_image_to_upload.chunks():
						algo2 = algo2+chunk
				
					path = default_storage.save(my_image_to_upload.name, ContentFile(algo2))
				
					try:
						os.makedirs(settings.PRIVATE_RECORD_ROOT + "/"+ r_id +"/" + 'genograma' + "/")
					except OSError as e:
						if e.errno == 17:
							pass
				
					os.rename(settings.MEDIA_ROOT + "/" + path, settings.PRIVATE_RECORD_ROOT + "/"+ r_id +"/" + 'genograma' +"/"+ path)
				
					answer.text_answer = "/"+ r_id +"/" + 'genograma' +"/"+ path
					answer.save()
				
		for my_table_field in my_table_fields:
			if(my_table_field.field_type == 7):
				num_col = my_table_field.number_columns
				num_fil = num_filas_tabla[my_table_field.id_form_table]
				name_table = my_table_field.form_table_identifier
				table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display, form_table_id_form_table=my_table_field.id_form_table)
				fila = 1
				for table_content in table_contents:
					if(num_col>=1):
						table_content.answer_col_1 = request.POST.get(name_table+"_col_"+str(fila)+"_1")
					if(num_col>=2):
						table_content.answer_col_2 = request.POST.get(name_table+"_col_"+str(fila)+"_2")
					if(num_col>=3):
						table_content.answer_col_3 = request.POST.get(name_table+"_col_"+str(fila)+"_3")
					if(num_col>=4):
						table_content.answer_col_4 = request.POST.get(name_table+"_col_"+str(fila)+"_4")
					if(num_col>=5):
						table_content.answer_col_5 = request.POST.get(name_table+"_col_"+str(fila)+"_5")
					if(num_col>=6):
						table_content.answer_col_6 = request.POST.get(name_table+"_col_"+str(fila)+"_6")
					if(num_col>=7):
						table_content.answer_col_7 = request.POST.get(name_table+"_col_"+str(fila)+"_7")
					fila = fila+1
					table_content.save()
			else:
				name_table = my_table_field.form_table_identifier
				num_col = my_table_field.number_columns
				num_fil_actual = int(request.POST.get("filas_"+name_table))
				num_fil_guardadas = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display, form_table_id_form_table=my_table_field.id_form_table).count()
				table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display, form_table_id_form_table=my_table_field.id_form_table)
				fila = 1
				for table_content in table_contents:
					content1 = content2 = content3 = content4 = content5 = content6 =  content7 = ""
					if(num_col>=1):
						content1 = request.POST.get(name_table+"_col_"+str(fila)+"_1")
						if(content1 == None):
							content1 = ""
						table_content.answer_col_1 = content1
					if(num_col>=2):
						content2 = request.POST.get(name_table+"_col_"+str(fila)+"_2")
						if(content2 == None):
							content2 = ""
						table_content.answer_col_2 = content2
					if(num_col>=3):
						content3 = request.POST.get(name_table+"_col_"+str(fila)+"_3")
						if(content3 == None):
							content3 = ""
						table_content.answer_col_3 = content3
					if(num_col>=4):
						content4 = request.POST.get(name_table+"_col_"+str(fila)+"_4")
						if(content4 == None):
							content4 = ""
						table_content.answer_col_4 = content4
					if(num_col>=5):
						content5 = request.POST.get(name_table+"_col_"+str(fila)+"_5")
						if(content5 == None):
							content5 = ""
						table_content.answer_col_5 = content5
					if(num_col>=6):
						content6 = request.POST.get(name_table+"_col_"+str(fila)+"_6")
						if(content6 == None):
							content6 = ""
						table_content.answer_col_6 = content6
					if(num_col>=7):
						content7 = request.POST.get(name_table+"_col_"+str(fila)+"_7")
						if(content7 == None):
							content7 = ""
						table_content.answer_col_7 = content7
					fila = fila+1
					if(not(content1==content2==content3==content4==content5==content6==content7=="")):
						table_content.save()
					else:
						table_content.delete()
				for x in range(num_fil_guardadas+1,num_fil_actual+1):
					my_insert2 = FormHasFormTable()
					my_insert2.form_id_form = my_form
					my_insert2.form_table_id_form_table = FormTable.objects.get(form_table_identifier = name_table)
					content1 = content2 = content3 = content4 = content5 = content6 =  content7 = ""
					if(num_col>=1):
						content1 = request.POST.get(name_table+"_col_"+str(x)+"_1")
						if(content1 == None):
							content1 = ""
						my_insert2.answer_col_1 = content1
					if(num_col>=2):
						content2 = request.POST.get(name_table+"_col_"+str(x)+"_2")
						if(content2 == None):
							content2 = ""
						my_insert2.answer_col_2 = content2
					if(num_col>=3):
						content3 = request.POST.get(name_table+"_col_"+str(x)+"_3")
						if(content3 == None):
							content3 = ""
						my_insert2.answer_col_3 = content3
					if(num_col>=4):
						content4 = request.POST.get(name_table+"_col_"+str(x)+"_4")
						if(content4 == None):
							content4 = ""
						my_insert2.answer_col_4 = content4
					if(num_col>=5):
						content5 = request.POST.get(name_table+"_col_"+str(x)+"_5")
						if(content5 == None):
							content5 = ""
						my_insert2.answer_col_5 = content5
					if(num_col>=6):
						content6 = request.POST.get(name_table+"_col_"+str(x)+"_6")
						if(content6 == None):
							content6 = ""
						my_insert2.answer_col_6 = content6
					if(num_col>=7):
						content7 = request.POST.get(name_table+"_col_"+str(x)+"_7")
						if(content7 == None):
							content7 = ""
						my_insert2.answer_col_7 = content7
					if(not(content1==content2==content3==content4==content5==content6==content7=="")):
						my_insert2.save()
              
			
		
		
    	
	#Cargar los campos 

	form_to_display = Form.objects.select_related("form_type_id_form_type").get(id_form=f_id)
	answers = FormHasField.objects.select_related("field_id_field").filter(form_id_form=form_to_display).order_by('field_id_field_id__field_number') #se cambio all por filter
	#table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display).order_by('form_table_id_form_table_id__field_number')
	form_fields = FormTable.objects.filter(form_type_id_form_type = form_to_display.form_type_id_form_type).order_by('field_number');
	both_answers = list(answers) + list(form_fields)
	#answers_sorted = sorted(both_answers,key=lambda x: x.field_id_field.field_number if hasattr(x, 'field_id_field') else x.form_table_id_form_table.field_number, reverse=False)
	answers_sorted = sorted(both_answers,key=lambda x: x.field_id_field.field_number if hasattr(x, 'field_id_field') else x.field_number, reverse=False)
	extra = []
	for temp_answer in answers_sorted:
		try:
			temp_answer.field_type == 7
			extra.append(FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display,form_table_id_form_table = temp_answer.id_form_table))
		except AttributeError:
			extra.append("")
			
	my_tuple = zip(answers_sorted,extra)	
	params = {'id_record' : r_id, 'identifier_record' : r, 'answer_fields' : answers_sorted, 'form_displaying' : form_to_display, 'answers_tuple' : my_tuple}
	return render(request,'sharedarea/record_edit.html',params)
	
def edit_summary(request,r,r_id,f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
		
	my_user = request.user
	my_record = Record.objects.get(id_record=r)
	
	#----Permiso
	if(my_record.student_id == None and my_record.professor_id == None):
		if not (my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.student_id == None):
		if not (my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	elif(my_record.professor == None):
		if not (my_user.id == my_record.student_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	else:
		if not (my_user.id == my_record.student_id or my_user.id == my_record.professor_id or my_user.groups.filter(name='Administrador').exists()):
			return redirect('/herramientas')
	
	my_summary = SummaryForm.objects.get(id_summary_form=f_id)
	my_form_type = FormType.objects.get(id_form_type=my_summary.form_type_id_form_type.id_form_type)
	if request.method == 'POST':
		form = summaryForm(request.POST, instance=my_summary)
		if form.is_valid():
			form.save()
	else:
		form = summaryForm(instance=my_summary)
	form_to_display = SummaryForm.objects.get(id_summary_form=f_id)
	params = {'id_record' : r_id, 'identifier_record' : r, 'form_displaying' : form_to_display, 'form': form}
	return render(request,'sharedarea/record_investigation_2.html',params)
		

def record_view_client(request,f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
	#Agregar valdacion de permisos

	my_user = request.user
	if Client.objects.filter(client_user=my_user.id).exists():
		my_client = Client.objects.get(client_user=my_user.id)
		my_record = Record.objects.get(client_id_client=my_client)
		
		forms = Form.objects.select_related("form_type_id_form_type").filter(record_id_record=my_record).exclude(form_type_id_form_type__visible_client = 0)
		forms_ids = Form.objects.select_related("form_type_id_form_type").filter(record_id_record=my_record, form_type_id_form_type__multiple=0).values('form_type_id_form_type__id_form_type')
		forms_missing = FormType.objects.filter(visible_client=1).exclude(id_form_type__in = forms_ids)
		form_to_display = None
		my_tuple = None
		if(f_id=='5' or f_id=='7'):
			my_form_type = FormType.objects.get(id_form_type=f_id)
			if Form.objects.select_related("form_type_id_form_type").filter(record_id_record = my_record, form_type_id_form_type = my_form_type).exists():
				form_to_display = Form.objects.select_related("form_type_id_form_type").get(record_id_record = my_record, form_type_id_form_type = my_form_type)
				
				
				answers = FormHasField.objects.select_related("field_id_field").filter(form_id_form=form_to_display).order_by('field_id_field_id__field_number') #se cambio all por filter
				#table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display).order_by('form_table_id_form_table_id__field_number')
				form_fields = FormTable.objects.filter(form_type_id_form_type=form_to_display.form_type_id_form_type).order_by('field_number');
				both_answers = list(answers) + list(form_fields)
				#answers_sorted = sorted(both_answers,key=lambda x: x.field_id_field.field_number if hasattr(x, 'field_id_field') else x.form_table_id_form_table.field_number, reverse=False)
				answers_sorted = sorted(both_answers,key=lambda x: x.field_id_field.field_number if hasattr(x, 'field_id_field') else x.field_number, reverse=False)
	
				extra = []
				for temp_answer in answers_sorted:
					try:
						temp_answer.field_type == 7
						extra.append(FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display,form_table_id_form_table = temp_answer.id_form_table))
					except AttributeError:
						extra.append("")
						
				my_tuple = zip(answers_sorted,extra)
				
		
		params = { 'forms_added' : forms, 'forms_missing' : forms_missing, 'form_displaying' : form_to_display, 'answers_tuple' : my_tuple}
		return render(request,'sharedarea/record_client_manager.html',params)
			
	else:
		return redirect('/herramientas')
	

def form_add_client(request):
	if (not request.user.is_authenticated()):
		return redirect('/')
	#Agregar validacion de permisos
	
	my_user = request.user
	
	if Client.objects.filter(client_user=my_user.id).exists():
		my_client = Client.objects.get(client_user=my_user.id)
		my_record = Record.objects.get(client_id_client=my_client)
	
	
		if request.method == 'POST':
			my_type = request.POST.get("form_identifier")
			if(my_type == None):
				return redirect('/herramientas')
		
			#Validar disponibilidad
			if not FormType.objects.filter(id_form_type=my_type, visible_client = 1).exists():
				int("")
				return redirect('/herramientas')
			
			my_form_type = FormType.objects.get(id_form_type=my_type)
		
		
			if(my_form_type.is_file==0):
				
				fields = Field.objects.filter(form_type_id_form_type = my_form_type).order_by('field_number');
				form_fields = FormTable.objects.filter(form_type_id_form_type = my_form_type).order_by('field_number');
				both_fields = list(fields) + list(form_fields)
				fields_sorted = sorted(both_fields, key=lambda x: x.field_number, reverse=False)
				params = {'identifier_record' : my_record.id_record, 'record_fields' : fields_sorted, 'my_form_type':my_form_type}
				return render(request,'sharedarea/record_add_client.html',params)
	return redirect('/herramientas')
	
def save_form_client(request, f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
		
	my_user = request.user
	
	if not Client.objects.filter(client_user=my_user.id).exists():
		return redirect('/')
		
	my_client = Client.objects.get(client_user=my_user.id)
	my_record = Record.objects.get(client_id_client=my_client)
	
	if request.method == 'POST':
		#Verificar de nuevo no se guarde uno que no se debe
		
		my_form_type = FormType.objects.get(id_form_type=f_id)
		
		if(not my_form_type.multiple):
			if(Form.objects.filter(form_type_id_form_type = my_form_type,record_id_record = my_record).exists()):
				return redirect('/herramientas')
		
		#Obtener campos del formato
		my_fields = Field.objects.filter(form_type_id_form_type = f_id)
		
		my_table_fields = FormTable.objects.filter(form_type_id_form_type = f_id).order_by('field_number')
		my_both_fields = list(my_fields) + list(my_table_fields)
		my_fields_sorted = sorted(my_both_fields, key=lambda x: x.field_number, reverse=False)
		
		#Listas para guardar contenido y errores
		my_errors = []
		my_contents = []
		error = False
		
		num_filas_tabla = {2:6, 6:12, 7:4, 8:24, 9:28, 10:30, 11:45, 12:9, 13:16, 15:8, 16:20, 19:11, 21:8}
		
		#Recorrer campos
		for my_field in my_fields_sorted:
			#verificar numero
			if(my_field.field_type == 2):
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				try:
					my_temp_val = int(content)
					my_errors.append("")
				except ValueError:
					error = True
					my_errors.append("Debe ingresar un número")
			elif(my_field.field_type == 4):
				content = request.POST.get(my_field.field_identifier)
				try:
					temp_date = datetime.strptime(content, "%d/%m/%Y")
					my_contents.append(temp_date.strftime("%d/%m/%Y"))
					my_errors.append("")
				except ValueError:
					error = True
					my_contents.append(content)
					my_errors.append("Debe ingresar una fecha con forma dd/mm/aaaa")
			elif(my_field.field_type == 12):
				try:
					my_image_to_upload = request.FILES[my_field.field_identifier]
					try:
						img = Image.open(my_image_to_upload)
						img.verify()
						my_contents.append("")
						my_errors.append("")
					except IOError:
						error = True
						my_contents.append("")
						my_errors.append("Debe subir una imagen")
				except MultiValueDictKeyError:
					my_contents.append("")
					my_errors.append("")
			elif(my_field.field_type == 7):
				num_col = my_field.number_columns
				num_fil = num_filas_tabla[my_field.id_form_table]
				name_table = my_field.form_table_identifier
				temp_table = []
				for x in range(1,num_fil+1):
					row = []
					for y in range(1, num_col+1):
						row.append(request.POST.get(name_table+"_col_"+str(x)+"_"+str(y)))
					temp_table.append(row)
				my_contents.append(temp_table)
				my_errors.append("")
				
			elif(my_field.field_type == 9):
				name_table = my_field.form_table_identifier
				temp_table = []
				num_col = my_field.number_columns
				num_fil = int(request.POST.get("filas_"+name_table))
				for x in range(1,num_fil+1):
					row = []
					for y in range(1, num_col+1):
						celda = request.POST.get(name_table+"_col_"+str(x)+"_"+str(y))
						if(celda == None):
							celda = ""
							row.append(celda)
						else:
							row.append(celda)
					temp_table.append(row)
				my_contents.append(temp_table)
				my_errors.append("")
			else:
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				my_errors.append("")
				
		#Hubo fallo y se mostraran errores
		if(error):
			my_tuple = zip(my_fields_sorted,my_contents,my_errors)	
			params = {'answer_tuple' : my_tuple, 'my_form_type':my_form_type}	
			return render(request,'sharedarea/record_add_client_2.html',params)
		
		#Encontrar expediente y tipo formato
		my_client = Client.objects.get(client_user=my_user.id)
		my_record = Record.objects.get(client_id_client=my_client)
		my_form_type = FormType.objects.get(id_form_type = f_id)
		
		#Crear Form
		my_form = Form()
		my_form.record_id_record = my_record
		my_form.form_type_id_form_type = my_form_type
		my_form.save()

		#Recorrer y guardar los campos
		for my_field in my_fields:
			if(not my_field.field_type == 12):
				content = request.POST.get(my_field.field_identifier)
			else:
				my_image_to_upload = request.FILES[my_field.field_identifier]
			my_insert = FormHasField()
			my_insert.form_id_form = my_form
			my_insert.field_id_field = my_field
			if(my_field.field_type == 1):
				my_insert.text_answer = content
			if(my_field.field_type == 2):
				my_insert.int_answer = content
			if(my_field.field_type == 4):
				temp_date = datetime.strptime(content, "%d/%m/%Y")
				my_insert.date_answer = temp_date.strftime("%Y-%m-%d")
			if(my_field.field_type == 5):
				if(content==None):
					my_insert.text_answer = ""
				else:
					my_insert.text_answer = content
			if(my_field.field_type == 6):
				my_insert.text_answer = content
			if(my_field.field_type == 11):
				my_insert.text_answer = content
			my_insert.save()
		for my_table_field in my_table_fields:
			if(my_table_field.field_type == 7):
				num_col = my_table_field.number_columns
				num_fil = num_filas_tabla[my_table_field.id_form_table]
				name_table = my_table_field.form_table_identifier
				for x in range(1,num_fil+1):
					my_insert2 = FormHasFormTable()
					my_insert2.form_id_form = my_form
					my_insert2.form_table_id_form_table = FormTable.objects.get(form_table_identifier = name_table)
					if(num_col>=1):
						content1 = request.POST.get(name_table+"_col_"+str(x)+"_1")
						my_insert2.answer_col_1 = content1
					if(num_col>=2):
						content2 = request.POST.get(name_table+"_col_"+str(x)+"_2")
						my_insert2.answer_col_2 = content2
					if(num_col>=3):
						content3 = request.POST.get(name_table+"_col_"+str(x)+"_3")
						my_insert2.answer_col_3 = content3
					if(num_col>=4):
						content4 = request.POST.get(name_table+"_col_"+str(x)+"_4")
						my_insert2.answer_col_4 = content4
					if(num_col>=5):
						content5 = request.POST.get(name_table+"_col_"+str(x)+"_5")
						my_insert2.answer_col_5 = content5
					if(num_col>=6):
						content6 = request.POST.get(name_table+"_col_"+str(x)+"_6")
						my_insert2.answer_col_6 = content6
					if(num_col>=7):
						content7 = request.POST.get(name_table+"_col_"+str(x)+"_7")
						my_insert2.answer_col_7 = content7
					my_insert2.save()
			else:
				name_table = my_table_field.form_table_identifier
				num_col = my_table_field.number_columns
				num_fil = int(request.POST.get("filas_"+name_table))
				for x in range(1,num_fil+1):
					my_insert2 = FormHasFormTable()
					my_insert2.form_id_form = my_form
					my_insert2.form_table_id_form_table = FormTable.objects.get(form_table_identifier = name_table)
					
					content1 = content2 = content3 = content4 = content5 = content6 =  content7 = ""
					if(num_col>=1):
						content1 = request.POST.get(name_table+"_col_"+str(x)+"_1")
						if(content1 == None):
							content1 = ""
						my_insert2.answer_col_1 = content1
					if(num_col>=2):
						content2 = request.POST.get(name_table+"_col_"+str(x)+"_2")
						if(content2 == None):
							content2 = ""
						my_insert2.answer_col_2 = content2
					if(num_col>=3):
						content3 = request.POST.get(name_table+"_col_"+str(x)+"_3")
						if(content3 == None):
							content3 = ""
						my_insert2.answer_col_3 = content3
					if(num_col>=4):
						content4 = request.POST.get(name_table+"_col_"+str(x)+"_4")
						if(content4 == None):
							content4 = ""
						my_insert2.answer_col_4 = content4
					if(num_col>=5):
						content5 = request.POST.get(name_table+"_col_"+str(x)+"_5")
						if(content5 == None):
							content5 = ""
						my_insert2.answer_col_5 = content5
					if(num_col>=6):
						content6 = request.POST.get(name_table+"_col_"+str(x)+"_6")
						if(content6 == None):
							content6 = ""
						my_insert2.answer_col_6 = content6
					if(num_col>=7):
						content7 = request.POST.get(name_table+"_col_"+str(x)+"_7")
						if(content7 == None):
							content7 = ""
						my_insert2.answer_col_7 = content7
					if(not(content1==content2==content3==content4==content5==content6==content7=="")):
						my_insert2.save()
		return redirect('/client_view/'+f_id)
						
def record_edit_client(request,f_id):
	if (not request.user.is_authenticated()):
		return redirect('/')
		
	my_user = request.user
	
	if not Client.objects.filter(client_user=my_user.id).exists():
		return redirect('/')
	
	my_client = Client.objects.get(client_user=my_user.id)
	my_record = Record.objects.get(client_id_client=my_client)
	
	my_form_type = FormType.objects.get(id_form_type=f_id)
    
	#En caso se deba guardar
	if request.method == 'POST':
		#----------Verificar todos los campos-----------
		num_filas_tabla = {2:6, 6:12, 7:4, 8:24, 9:28, 10:30, 11:45, 12:9, 13:16, 15:8, 16:20, 19:11, 21:8}
		
		#Obtener los campos del formato (campos y tablas en orden)
		my_form = Form.objects.get(record_id_record=my_record,form_type_id_form_type=my_form_type)
		my_fields = Field.objects.filter(form_type_id_form_type = my_form_type).order_by('field_number')
		my_table_fields = FormTable.objects.filter(form_type_id_form_type = my_form_type).order_by('field_number')
		my_both_fields = list(my_fields) + list(my_table_fields)
		my_fields_sorted = sorted(my_both_fields, key=lambda x: x.field_number, reverse=False)
		#Recorrer campos
		my_errors = []
		my_contents = []
		error = False
		for my_field in my_fields_sorted:
		#verificar numero
			if(my_field.field_type == 2):
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				try:
					my_temp_val = int(content)
					my_errors.append("")
				except ValueError:
					error = True
					my_errors.append("Debe ingresar un número")
			elif(my_field.field_type == 4):
				content = request.POST.get(my_field.field_identifier)
				
				try:
					temp_date = datetime.strptime(content, "%d/%m/%Y")
					my_contents.append(temp_date.strftime("%d/%m/%Y"))
					my_errors.append("")
					#temp_date=parse_date(content)
					#if(temp_date==None):
					#	error = True
					#	int("")
					#	my_errors.append("Debe ingresar una fecha con forma dd-mm-aaaa")
					#else:
					#	my_errors.append("")
				except ValueError:
					error = True
					my_contents.append(content)
					my_errors.append("Debe ingresar una fecha con forma dd-mm-aaaa")
			elif(my_field.field_type == 12):
				try:
					my_image_to_upload = request.FILES[my_field.field_identifier]
					try:
						img = Image.open(my_image_to_upload)
						img.verify()
						my_contents.append("")
						my_errors.append("")
					except IOError:
						error = True
						my_contents.append("")
						my_errors.append("Debe subir una imagen")
				except MultiValueDictKeyError:
					my_contents.append("")
					my_errors.append("")
			elif(my_field.field_type == 7):
				num_col = my_field.number_columns
				num_fil = num_filas_tabla[my_field.id_form_table]
				name_table = my_field.form_table_identifier
				temp_table = []
				for x in range(1,num_fil+1):
					row = []
					for y in range(1, num_col+1):
						row.append(request.POST.get(name_table+"_col_"+str(x)+"_"+str(y)))
					temp_table.append(row)
				my_contents.append(temp_table)
				my_errors.append("")
			elif(my_field.field_type == 9):
				name_table = my_field.form_table_identifier
				temp_table = []
				num_col = my_field.number_columns
				num_fil = int(request.POST.get("filas_"+name_table))
				for x in range(1,num_fil+1):
					row = []
					for y in range(1, num_col+1):
						celda = request.POST.get(name_table+"_col_"+str(x)+"_"+str(y))
						if(celda == None):
							celda = ""
							row.append(celda)
						else:
							row.append(celda)
						
					temp_table.append(row)
				my_contents.append(temp_table)
				my_errors.append("")
			else:
				content = request.POST.get(my_field.field_identifier)
				my_contents.append(content)
				my_errors.append("")
		
		#Hubo fallo y se mostraran errores
		if(error):
			form_to_display = Form.objects.select_related("form_type_id_form_type").get(record_id_record=my_record,form_type_id_form_type=my_form_type)
			my_tuple = zip(my_fields_sorted,my_contents,my_errors)	
			params = {'answer_tuple' : my_tuple, 'form_displaying' : form_to_display}	
			return render(request,'sharedarea/record_edit_client_2.html',params)		
		#Actualizar campos
		form_to_display = Form.objects.select_related("form_type_id_form_type").get(record_id_record=my_record,form_type_id_form_type=my_form_type)
		answers = FormHasField.objects.select_related("field_id_field").filter(form_id_form=form_to_display)
		table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display)
		for answer in answers:
			if(answer.field_id_field.field_type==1):
				answer.text_answer = request.POST.get(answer.field_id_field.field_identifier)
				answer.save()
			elif(answer.field_id_field.field_type==2):
				answer.int_answer = request.POST.get(answer.field_id_field.field_identifier)
				answer.save()
			elif(answer.field_id_field.field_type==4):
				content = request.POST.get(answer.field_id_field.field_identifier)
				temp_date = datetime.strptime(content, "%d/%m/%Y")
				answer.date_answer = temp_date.strftime("%Y-%m-%d")
				answer.save()
			elif(answer.field_id_field.field_type==5):
				content = request.POST.get(answer.field_id_field.field_identifier)
				if(content==None):
					answer.text_answer = ""
				else:
					answer.text_answer = content
				answer.save()
			elif(answer.field_id_field.field_type==6):
				answer.text_answer = request.POST.get(answer.field_id_field.field_identifier)
				answer.save()
			elif(answer.field_id_field.field_type==11):
				answer.text_answer = request.POST.get(answer.field_id_field.field_identifier)
				answer.save()
				
		for my_table_field in my_table_fields:
			if(my_table_field.field_type == 7):
				num_col = my_table_field.number_columns
				num_fil = num_filas_tabla[my_table_field.id_form_table]
				name_table = my_table_field.form_table_identifier
				table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display, form_table_id_form_table=my_table_field.id_form_table)
				fila = 1
				for table_content in table_contents:
					if(num_col>=1):
						table_content.answer_col_1 = request.POST.get(name_table+"_col_"+str(fila)+"_1")
					if(num_col>=2):
						table_content.answer_col_2 = request.POST.get(name_table+"_col_"+str(fila)+"_2")
					if(num_col>=3):
						table_content.answer_col_3 = request.POST.get(name_table+"_col_"+str(fila)+"_3")
					if(num_col>=4):
						table_content.answer_col_4 = request.POST.get(name_table+"_col_"+str(fila)+"_4")
					if(num_col>=5):
						table_content.answer_col_5 = request.POST.get(name_table+"_col_"+str(fila)+"_5")
					if(num_col>=6):
						table_content.answer_col_6 = request.POST.get(name_table+"_col_"+str(fila)+"_6")
					if(num_col>=7):
						table_content.answer_col_7 = request.POST.get(name_table+"_col_"+str(fila)+"_7")
					fila = fila+1
					table_content.save()
			else:
				name_table = my_table_field.form_table_identifier
				num_col = my_table_field.number_columns
				num_fil_actual = int(request.POST.get("filas_"+name_table))
				num_fil_guardadas = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display, form_table_id_form_table=my_table_field.id_form_table).count()
				table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display, form_table_id_form_table=my_table_field.id_form_table)
				fila = 1
				for table_content in table_contents:
					content1 = content2 = content3 = content4 = content5 = content6 =  content7 = ""
					if(num_col>=1):
						content1 = request.POST.get(name_table+"_col_"+str(fila)+"_1")
						if(content1 == None):
							content1 = ""
						table_content.answer_col_1 = content1
					if(num_col>=2):
						content2 = request.POST.get(name_table+"_col_"+str(fila)+"_2")
						if(content2 == None):
							content2 = ""
						table_content.answer_col_2 = content2
					if(num_col>=3):
						content3 = request.POST.get(name_table+"_col_"+str(fila)+"_3")
						if(content3 == None):
							content3 = ""
						table_content.answer_col_3 = content3
					if(num_col>=4):
						content4 = request.POST.get(name_table+"_col_"+str(fila)+"_4")
						if(content4 == None):
							content4 = ""
						table_content.answer_col_4 = content4
					if(num_col>=5):
						content5 = request.POST.get(name_table+"_col_"+str(fila)+"_5")
						if(content5 == None):
							content5 = ""
						table_content.answer_col_5 = content5
					if(num_col>=6):
						content6 = request.POST.get(name_table+"_col_"+str(fila)+"_6")
						if(content6 == None):
							content6 = ""
						table_content.answer_col_6 = content6
					if(num_col>=7):
						content7 = request.POST.get(name_table+"_col_"+str(fila)+"_7")
						if(content7 == None):
							content7 = ""
						table_content.answer_col_7 = content7
					fila = fila+1
					if(not(content1==content2==content3==content4==content5==content6==content7=="")):
						table_content.save()
					else:
						table_content.delete()
				for x in range(num_fil_guardadas+1,num_fil_actual+1):
					my_insert2 = FormHasFormTable()
					my_insert2.form_id_form = my_form
					my_insert2.form_table_id_form_table = FormTable.objects.get(form_table_identifier = name_table)
					content1 = content2 = content3 = content4 = content5 = content6 =  content7 = ""
					if(num_col>=1):
						content1 = request.POST.get(name_table+"_col_"+str(x)+"_1")
						if(content1 == None):
							content1 = ""
						my_insert2.answer_col_1 = content1
					if(num_col>=2):
						content2 = request.POST.get(name_table+"_col_"+str(x)+"_2")
						if(content2 == None):
							content2 = ""
						my_insert2.answer_col_2 = content2
					if(num_col>=3):
						content3 = request.POST.get(name_table+"_col_"+str(x)+"_3")
						if(content3 == None):
							content3 = ""
						my_insert2.answer_col_3 = content3
					if(num_col>=4):
						content4 = request.POST.get(name_table+"_col_"+str(x)+"_4")
						if(content4 == None):
							content4 = ""
						my_insert2.answer_col_4 = content4
					if(num_col>=5):
						content5 = request.POST.get(name_table+"_col_"+str(x)+"_5")
						if(content5 == None):
							content5 = ""
						my_insert2.answer_col_5 = content5
					if(num_col>=6):
						content6 = request.POST.get(name_table+"_col_"+str(x)+"_6")
						if(content6 == None):
							content6 = ""
						my_insert2.answer_col_6 = content6
					if(num_col>=7):
						content7 = request.POST.get(name_table+"_col_"+str(x)+"_7")
						if(content7 == None):
							content7 = ""
						my_insert2.answer_col_7 = content7
					if(not(content1==content2==content3==content4==content5==content6==content7=="")):
						my_insert2.save()
              
			
		
		
    	
	#Cargar los campos 

	form_to_display = Form.objects.select_related("form_type_id_form_type").get(record_id_record=my_record,form_type_id_form_type=my_form_type)
	answers = FormHasField.objects.select_related("field_id_field").filter(form_id_form=form_to_display).order_by('field_id_field_id__field_number') #se cambio all por filter
	#table_contents = FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display).order_by('form_table_id_form_table_id__field_number')
	form_fields = FormTable.objects.filter(form_type_id_form_type = form_to_display.form_type_id_form_type).order_by('field_number');
	both_answers = list(answers) + list(form_fields)
	#answers_sorted = sorted(both_answers,key=lambda x: x.field_id_field.field_number if hasattr(x, 'field_id_field') else x.form_table_id_form_table.field_number, reverse=False)
	answers_sorted = sorted(both_answers,key=lambda x: x.field_id_field.field_number if hasattr(x, 'field_id_field') else x.field_number, reverse=False)
	extra = []
	for temp_answer in answers_sorted:
		try:
			temp_answer.field_type == 7
			extra.append(FormHasFormTable.objects.select_related("form_table_id_form_table").filter(form_id_form=form_to_display,form_table_id_form_table = temp_answer.id_form_table))
		except AttributeError:
			extra.append("")
			
	my_tuple = zip(answers_sorted,extra)	
	params = {'answer_fields' : answers_sorted, 'form_displaying' : form_to_display, 'answers_tuple' : my_tuple}
	return render(request,'sharedarea/record_edit_client.html',params)

	

	
