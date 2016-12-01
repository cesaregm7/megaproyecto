# -*- coding: utf-8 -*-
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from testarea.forms import *
from sharedarea.models import *
from django.views.decorators.http import require_http_methods
import random

# Create your views here.

def consentimiento_test_preliminar(request,test):
	nombre =  "nada"
	url = "nada"
	params = {'nombre_test' : nombre,
	     		 'url_test' : url}
	if test == "1" or test == "2" or test == "3":
		return render(request, 'sharedarea/test_consentimiento_informado.html', {'test_id':test})
	else:
		test = Test.objects.filter(id_test=int(test))[0]
		params = {'nombre_test' : test.name,
				  'test_id':test.id_test}
		return render(request,'sharedarea/test_preliminar/test_consentimiento_informado.html', params)

	#if test == "0":
	#	nombre =  "Trastorno de atencion"
	#	url = "test_preliminar"
	#elif test == "1":
	#	nombre =  "Autismo"
		#url = "test_preliminar"
	#elif test == "2":
	#	nombre =  "Trastorno de aprendizaje"
	#	url = "test_preliminar"
	#params = {'nombre_test' : nombre,
	#      		 'url_test' : url}

@require_http_methods(["POST"])
def formulario_demografico(request, test):
	form = TestDemograficForm(request.POST or None)
	return render(request, 'sharedarea/test_preliminar/test_formulario_demografico.html', {'form': form, 'test_id': test})


@require_http_methods(["POST"])
def test_preliminar(request, test):
	form = TestDemograficForm(request.POST or None)
	if form.is_valid():
		#form.save()
		test_object = Test.objects.filter(id_test=test)[0]
		questions = TestQuestions.objects.filter(test_id_test=test)	
		params = {'test' : test_object,
		  		  'questions' : questions,
				  'form' : form,
				  'questions_range' : range(0,test_object.max_val)}
		return render(request,'sharedarea/test_preliminar/index_test_preliminar.html', params)
		#return HttpResponseRedirect(url)
	else:
		url = reverse('testarea:formulario_demografico')
		return HttpResponseRedirect(url)


	test = Test.objects.filter(id_test=0)[0]
	questions = TestQuestions.objects.filter(test_id_test=0)	
	params = {'test' : test,
      		  'questions' : questions,
			  'questions_range' : range(0,test.max_val)}
	return render(request,'sharedarea/test_preliminar/index_test_preliminar.html', params)

@require_http_methods(["POST"])
def test_organizaciones(request, test):
	form = TestGeneralForm(request.POST or None)
	if form.is_valid():
		#form.save()
		test = Test.objects.filter(id_test=test)[0]
		questions = TestQuestions.objects.filter(test_id_test=test)	
		params = {'test' : test,
		  		  'questions' : questions,
				  'form' : form,
				  'questions_range' : range(0,test.max_val)}
		return render(request,'sharedarea/test_preliminar/index_test_preliminar.html', params)
		#return HttpResponseRedirect(url)
	else:
		url = reverse('testarea:formulario_general')
		return HttpResponseRedirect(url)


	test = Test.objects.filter(id_test=test)[0]
	questions = TestQuestions.objects.filter(test_id_test=test)	
	params = {'test' : test,
      		  'questions' : questions,
			  'questions_range' : range(0,test.max_val)}
	return render(request,'sharedarea/test_preliminar/index_test_preliminar.html', params)

def resultados_organizacional(request):
	idTest = int(request.POST["test_id"])
	test = Test.objects.filter(id_test=idTest)[0]
	title =""

	#Examen Acoso Laboral
	if(idTest==1):
		total = 0
		results = [["Desacreditación", "Son actividades de acoso dirigidas a desacreditar o impedir a la víctima mantener su reputación personal o laboral"],
					["Política Organizacional", "Son las acciones que se toman dentro de la organización, que son partes de las políticas"],
					["Información y Actuaciones ante el acoso", "Son las acciones que la víctima o compañeros de trabajo efectúan para detener las actividades de acoso"],
					["Consecuencias", "Son actividades de acoso que afectan a la salud física o psíquica de la víctima"]]
		aislamiento = 0
		exigencia = 0
		desacreditacion = 0
		politica = 0
		actuaciones = 0
		consecuencias = 0
		for key in request.POST:
			if key.isdigit():
				if(int(key) >=4 and int(key) <=8):
					aislamiento +=int(request.POST[key])+1
				elif(int(key) >=9 and int(key) <=12):
					exigencia +=int(request.POST[key]) +1
				elif(int(key) >=13 and int(key) <=16):
					desacreditacion +=int(request.POST[key])+1
				elif(int(key) >=17 and int(key) <=21):
					politica +=int(request.POST[key])+1
				elif(int(key) >=22 and int(key) <=24):
					actuaciones +=int(request.POST[key])+1
				elif(int(key) >=25 and int(key) <=26):
					consecuencias += int(request.POST[key])+1
		answers = [aislamiento, exigencia, desacreditacion, politica, actuaciones, consecuencias]
		title = "Resultados Acoso Laboral"
		total = aislamiento + exigencia + desacreditacion + politica + actuaciones + consecuencias
		if (total>=0 and total <=23):
			screening = "Déficit"
		elif (total>=24 and total <=46):
			screening = "Necesidad de Mejorar"
		elif (total >=47 and total <=69):
			screening = "No existe signo de acoso laboral"
	elif(idTest==2):
		total = 0
		results = [["Presión", "La percepción que existe con respecto a los estándares de desempeño, funcionamiento y finalización de la tarea."],
					["Equidad", "La percepción que los empleados tienen, acerca de sí existen políticas y reglamentos equitativos y claros dentro de la institución."],
					["Autonomía", "Percepción del trabajador acerca de la autodeterminación y responsabilidad necesaria en la toma de decisiones con respecto a procedimientos del trabajo, metas y prioridades."],
					["Confianza", "La percepción de la libertad para comunicarse abiertamente con los superiores, para tratar temas sensibles o personales con la confidencia suficiente de que esa comunicación no será violada o usada en contra de los miembros."],
					["Reconocimiento", "La percepción que tienen los miembros de la organización, con respecto a la recompensa que reciben, por su contribución a la empresa."],
					["Innovación", "La percepción que se tiene acerca del ánimo que se tiene para asumir riesgos, ser creativo y asumir nuevas áreas de trabajo, en dónde tenga poco o nada de experiencia."],
					["Cohesión", "Percepción de las relaciones entre los trabajadores dentro de la organización, la existencia de una atmósfera amigable y de confianza y proporción de ayuda material en la realización de las tareas."],
					["Apoyo", "La percepción que tienen los miembros acerca del respaldo y tolerancia en el comportamiento dentro de la institución, esto incluye el aprendizaje de los errores, por parte del trabajador, sin miedo a la represalia de sus superiores o compañeros de trabajo."]]

		autonomia = 0
		cohesion = 0
		confianza = 0
		presion = 0
		apoyo = 0 
		reconocimiento = 0
		equidad =0
		innovacion = 0
		for key in request.POST:
			if key.isdigit():
				if(int(key) >=27 and int(key) <=31):
					autonomia +=int(request.POST[key]) +1
				elif(int(key) >=32 and int(key) <=36):
					cohesion +=int(request.POST[key]) +1
				elif(int(key) >=37 and int(key) <=41):
					confianza +=int(request.POST[key]) +1
				elif(int(key) >=42 and int(key) <=46):
					presion +=int(request.POST[key])
				elif(int(key) >=47 and int(key) <=51):
					apoyo +=int(request.POST[key]) +1
				elif(int(key) >=52 and int(key) <=56):
					reconocimiento += int(request.POST[key]) +1
				elif(int(key) >=57 and int(key) <=61):
					equidad +=int(request.POST[key]) +1
				elif(int(key) >=62 and int(key) <=66):
					innovacion += int(request.POST[key]) +1
		answers = [autonomia, cohesion, confianza, presion, apoyo, reconocimiento, equidad, innovacion]
		title = "Resultados Clima Laboral"
		total = autonomia + cohesion + confianza + presion + apoyo + reconocimiento + equidad + innovacion
		if (total>=0 and total <=40):
			screening = "Déficit"
		elif (total>=41 and total <=80):
			screening = "Necesidad de Mejorar"
		elif (total >=81 and total <=120):
			screening = "Clima laboral Agradable"
	elif(idTest==3):
		total = 0
		results = [["Cansancio Emocional", "Desequilibrio entre la percepción de las capacidades de afrontamiento, recursos físicos y mentales de los trabajadores ante las exigencias de su actividad."],
					["Despersonalización", "Sentimientos de impotencia, indefensión y desesperanza personal."],
					["Realización Personal","Pérdida de ideales, alejamiento de actividades familiares, sociales y recreativas."]]	
		cansancio = 0
		despersonalizacion = 0
		realizacion = 0
		for key in request.POST:
			if key.isdigit():
				if(int(key) >=67 and int(key) <=75):
					cansancio +=int(request.POST[key]) +1
				elif(int(key) >=76 and int(key) <=80):
					despersonalizacion +=int(request.POST[key]) +1
				elif(int(key) >=81 and int(key) <=88):
					realizacion +=int(request.POST[key]) +1
		answers = [cansancio, despersonalizacion, realizacion]
		title = "Resultados Desgaste Laboral"
		total = cansancio + despersonalizacion + realizacion
		if (total>=0 and total <=22):
			screening = "Déficit"
		elif (total>=23 and total <=44):
			screening = "Necesidad de Mejorar"
		elif (total >=45 and total <=66):
			screening = "No existe signo de desgaste laboral"

	lastId = TestResult.objects.latest('id_test_result')
	formTest = TestResult()
	formTest.id_test_result = lastId.pk + 1
	formTest.resultado = screening
	formTest.test_id_test = Test.objects.filter(id_test=int(request.POST["test_id"]))[0]
	formTest.save()

	form = TestOrganizationGeneralForm()
	form.name = request.POST['name']
	form.last_name = request.POST['last_name']
	form.age = request.POST['age']
	form.gender = request.POST['gender']
	form.marital_status = request.POST['marital_status']
	form.education = request.POST['education']
	form.job = request.POST['job']
	form.working_time = request.POST['working_time']
	form.organization_size = request.POST['organization_size']
	form.organization_type = request.POST['organization_type']
	form.test_result_id_test_result = formTest
	form.save()


	params = {'idTest': idTest, 'title': title, 'screening': screening, 'answers': answers, 'results': results}
	return render(request,'sharedarea/test_result_org.html', params)

def resultados_clinica(request):
	lista_riesgo = ["sin riesgo"
				   ,"riesgo leve"
				   ,"riesgo moderado"
				   ,"riesgo alto"
				   ,"nivel bajo"
				   ,"nivel medio-bajo"
				   ,"nivel medio"
				   ,"nivel alto"]

	lista_colores = ["73a839"
					,"ffff06"
					,"dd5600"
					,"c71c22"]

	test = Test.objects.filter(id_test=int(request.POST["test_id"]))[0]
	ans = 0
	count = 0
	for key in request.POST:
		if key.isdigit():
			ans += int(request.POST[key])
			count += 1
	
	res = float(ans)/float(count)
	
	test_result = 0
	tipo_riesgo = ""


	if res >= 0.0 and res < 1.0:
		test_result = 0
	elif res >= 1.0 and res < 2.0:
		test_result = 1
	elif res >= 2.0 and res < 3.0:
		test_result = 2
	elif res >= 3.0 and res < 4.0:
		test_result = 3

	color = lista_colores[test_result]
	percentage = round(100.0 * (float(test_result+1) / 4.0), 2)

	if test.id_test == 7:
		test_result += 4
		color = lista_colores[3 - test_result]

	tipo_riesgo = lista_riesgo[test_result]
	test_result = TestResult.objects.filter(id_test_result=test_result)[0]
	recomendations = Recomendation.objects.filter(id_test_recomendation=test)
	s_recomendation = random.choice(recomendations)

	params = {'test' : test,
			  'percentage' : percentage,
			  'color' : color,
			  'test_result' : test_result,
			  'tipo_riesgo' : tipo_riesgo,
			  'recomendation' : s_recomendation}

	#Guardar demografico
	new_result = TestDemograficResult()
	new_result.age = request.POST["age"]
	new_result.gender = request.POST["gender"]
	new_result.relationship = request.POST["relationship"]
	new_result.test_result_id_test_result =test_result
	new_result.test_id_test = test
	new_result.result = res

	new_result.save()

	return render(request,'sharedarea/test_preliminar/index_test_results.html', params)

def test_result(request):
	if request.POST:
		test_id = request.POST["test_id"]
		if test_id == "1" or test_id == "2" or test_id == "3":
			return resultados_organizacional(request)
		else:
			return resultados_clinica(request)
	else:
		return render(request, 'sharedarea/test_consentimiento_informado.html')


def consentimiento_informado(request):
	return render(request, 'sharedarea/test_consentimiento_informado.html')
	
@require_http_methods(["POST"])
def formulario_general(request, test):
	form = TestGeneralForm(request.POST or None)
	return render(request, 'sharedarea/test_formulario_general.html', {'form': form, 'test_id': test})

def descargar_test(request):
	if request.user.groups.filter(name='Administrador').exists():
		if request.method == "POST":
		   # Create the HttpResponse object with the appropriate CSV header.
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="Resultados tests.csv"'

			writer = csv.writer(response)

			results = TestDemograficResult.objects.all()
			field_names = ["Id","Edad","Genero","Relacion con el niño","Test realizado","Resultado"]
			writer.writerow(field_names)
			for obj in results:
				writer.writerow([getattr(obj, 'id_test_demografic_result'),
								 getattr(obj, 'age'),
								 getattr(obj, 'gender'),
								 getattr(obj, 'relationship'),
								 getattr(obj, 'test_id_test'),
								 getattr(obj, 'result')])
			return response
		else:
			return render (request, 'sharedarea/test_preliminar/index_test_download.html')

