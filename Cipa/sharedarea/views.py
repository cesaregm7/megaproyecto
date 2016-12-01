# -*- coding: utf-8 -*-
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import now
from datetime import datetime
from sharedarea import forms
from sharedarea.models import *
from django.db.models import Q

def index(request):
    return render(request,'sharedarea/index_content.html')

def herramientas(request):
	return render(request,'sharedarea/herramientas.html')

def servicio_organizaciones(request):
    return render(request,'sharedarea/servicio_org.html')

def servicio_educativo(request):
	tests = Test.objects.filter(Q(id_test=0) |
								Q(id_test=4) |
								Q(id_test=5) |
								Q(id_test=6) |
								Q(id_test=7))
	params = {'tests' : tests}
	return render(request,'sharedarea/servicio_edu.html', params)

def servicio_psicoterapia(request):
	return render(request,'sharedarea/servicio_psi.html')

def fichas_tecnicas(request):
	documentos = Documents.objects.filter(id_documents__lte=72)
	phg = documentos.filter(keywords='Pruebas de Habilidades Generales')
	phgnv = documentos.filter(keywords='Pruebas de Habilidades Generales No Verbales')
	phpc = documentos.filter(keywords='Pruebas de Habilidades/Procesos Cognitivos')
	pda = documentos.filter(keywords='Pruebas de Aprovechamiento')
	pdvm = documentos.filter(keywords='Pruebas de Viso Motricidad')
	pdat = documentos.filter(keywords='Pruebas de Atención')
	pdm = documentos.filter(keywords='Pruebas de Memoria')
	pdlyl = documentos.filter(keywords='Pruebas de Lectura y Lenguaje')
	pdp = documentos.filter(keywords='Pruebas de Personalidad')
	pp = documentos.filter(keywords='Pruebas Proyectivas')
	pdedd = documentos.filter(keywords='Pruebas de Evaluación del Desarrollo')
	pn = documentos.filter(keywords='Pruebas Neurológicas')
	iyhde = documentos.filter(keywords='Inventario y Hábitos de Estudio')
	idap = documentos.filter(keywords='Inventario de Aptitudes Primarias (Valores)')
	types = [{"text":'Pruebas de Habilidades Generales',"id":1},{"text":'Pruebas de Habilidades Generales No Verbales',"id":2},{"text":'Pruebas de Habilidades/Procesos Cognitivos',"id":3},{"text":'Pruebas de Aprovechamiento',"id":4},{"text":'Pruebas de Viso Motricidad',"id":5},{"text":'Pruebas de Atención',"id":6},{"text":'Pruebas de Memoria',"id":7},{"text":'Pruebas de Lectura y Lenguaje',"id":8},{"text":'Pruebas de Personalidad',"id":9},{"text":'Pruebas Proyectivas',"id":10},{"text":'Pruebas de Evaluación del Desarrollo',"id":11},{"text":'Pruebas Neurológicas',"id":12},{"text":'Inventario y Hábitos de Estudio',"id":13},{"text":'Inventario de Aptitudes Primarias (Valores)',"id":14}]
	params = {"phg":phg,"phgnv":phgnv,"phpc":phpc,"pda":pda,"pdvm":pdvm,"pdat":pdat,"pdm":pdm,"pdlyl":pdlyl,"pdp":pdp,"pp":pp,"pdedd":pdedd,"pn":pn,"iyhde":iyhde,"idap":idap,"types":types}
	return render(request,'sharedarea/fichas_tecnicas.html',params)

def generar_diploma(request):
    iduser = request.user.pk
    induccion = Induction.objects.filter(auth_user=iduser)[0]
    bandera = False
    if induccion.module_1>=5 and induccion.module_2>=5 and induccion.module_3>=5 and induccion.module_4>=4:
        bandera = True
    params = {"induccion":induccion,"usuario":request.user.username,"aprobado":bandera}
    if induccion.module_1>=5 and induccion.module_2>=5 and induccion.module_3>=5 and induccion.module_4>=4:
        return render(request,'sharedarea/diploma.html',params)
    else:
        return render(request,'sharedarea/induccion_intro.html',params)

def evaluar_test1(request):
    r1 = request.POST.get('q1', False)
    r2 = request.POST.get('q2', False)
    r3 = request.POST.get('q3', False)
    r4 = request.POST.get('q4', False)
    r5 = request.POST.get('q5', False)
    r6 = request.POST.get('q6', False)
    r7 = request.POST.get('q7', False)
    r8 = request.POST.get('q8', False)
    contador = 0
    if r1 == "3":
        contador+=1
    if r2 == "4":
        contador+=1
    if r3 == "1":
        contador+=1
    if r4 == "3":
        contador+=1
    if r5 == "4":
        contador+=1
    if r6 == "4":
        contador+=1
    if r7 == "2":
        contador+=1
    if r8 == "4":
        contador+=1
    iduser = request.user.pk
    #fields = AuthUser.objects.all();
    induccion = Induction.objects.filter(auth_user=iduser)[0]
    induccion.module_1 = contador
    induccion.save()
    bandera = False
    if induccion.module_1>=5 and induccion.module_2>=5 and induccion.module_3>=5 and induccion.module_4>=4:
        bandera = True
        induccion.approved_date = datetime.now()
        induccion.save()
    params = {"induccion":induccion,"usuario":request.user.username,"aprobado":bandera}
    return redirect('/induccion')

def evaluar_test2(request):
    r1 = request.POST.get('q1', False)
    r2 = request.POST.get('q2', False)
    r3 = request.POST.get('q3', False)
    r4 = request.POST.get('q4', False)
    r5 = request.POST.get('q5', False)
    r6 = request.POST.get('q6', False)
    r7 = request.POST.get('q7', False)
    r8 = request.POST.get('q8', False)
    contador = 0
    if r1 == "1":
        contador+=1
    if r2 == "2":
        contador+=1
    if r3 == "4":
        contador+=1
    if r4 == "3":
        contador+=1
    if r5 == "4":
        contador+=1
    if r6 == "2":
        contador+=1
    if r7 == "1":
        contador+=1
    if r8 == "2":
        contador+=1
    iduser = request.user.pk
    #fields = AuthUser.objects.all();
    induccion = Induction.objects.filter(auth_user=iduser)[0]
    induccion.module_2 = contador
    induccion.save()
    bandera = False
    if induccion.module_1>=5 and induccion.module_2>=5 and induccion.module_3>=5 and induccion.module_4>=4:
        bandera = True
        induccion.approved_date = datetime.now()
        induccion.save()
    params = {"induccion":induccion,"usuario":request.user.username,"aprobado":bandera}
    return redirect('/induccion')

def evaluar_test3(request):
    r1 = request.POST.get('q1', False)
    r2 = request.POST.get('q2', False)
    r3 = request.POST.get('q3', False)
    r4 = request.POST.get('q4', False)
    r5 = request.POST.get('q5', False)
    r6 = request.POST.get('q6', False)
    r7 = request.POST.get('q7', False)
    r8 = request.POST.get('q8', False)
    contador = 0
    if r1 == "3":
        contador+=1
    if r2 == "4":
        contador+=1
    if r3 == "4":
        contador+=1
    if r4 == "1":
        contador+=1
    if r5 == "4":
        contador+=1
    if r6 == "2":
        contador+=1
    if r7 == "3":
        contador+=1
    if r8 == "1":
        contador+=1
    iduser = request.user.pk
    #fields = AuthUser.objects.all();
    induccion = Induction.objects.filter(auth_user=iduser)[0]
    induccion.module_3 = contador
    induccion.save()
    bandera = False
    if induccion.module_1>=5 and induccion.module_2>=5 and induccion.module_3>=5 and induccion.module_4>=4:
        bandera = True
        induccion.approved_date = datetime.now()
        induccion.save()
    params = {"induccion":induccion,"usuario":request.user.username,"aprobado":bandera}
    return redirect('/induccion')

def evaluar_test4(request):
    r1 = request.POST.get('q1', False)
    r2 = request.POST.get('q2', False)
    r3 = request.POST.get('q3', False)
    r4 = request.POST.get('q4', False)
    r5 = request.POST.get('q5', False)
    r6 = request.POST.get('q6', False)
    contador = 0
    if r1 == "3":
        contador+=1
    if r2 == "4":
        contador+=1
    if r3 == "4":
        contador+=1
    if r4 == "2":
        contador+=1
    if r5 == "3":
        contador+=1
    if r6 == "2":
        contador+=1
    iduser = request.user.pk
    #fields = AuthUser.objects.all();
    induccion = Induction.objects.filter(auth_user=iduser)[0]
    induccion.module_4 = contador
    induccion.save()
    bandera = False
    if induccion.module_1>=5 and induccion.module_2>=5 and induccion.module_3>=5 and induccion.module_4>=4:
        bandera = True
        induccion.approved_date = datetime.now()
        induccion.save()
    params = {"induccion":induccion,"usuario":request.user.username,"aprobado":bandera}
    return redirect('/induccion')
    
def login_user(request):
	if (request.user.is_authenticated()):
		return redirect('/herramientas')
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/herramientas')
			else:
				#Return a 'disabled account' error message
				message = "disabled account"
				return redirect('/')
		else:
			#Return an 'invalid login' error message.
			message = "invalid login"
			return render(request, 'sharedarea/login.html')
	return render(request, 'sharedarea/login.html')

def induccion_intro(request):
    iduser = request.user.pk
    #fields = AuthUser.objects.all();
    induccionaux = Induction.objects.filter(auth_user=iduser)
    if not induccionaux:
        user = AuthUser.objects.filter(username = request.user.username)[0]
        induccion = Induction(module_1=0,module_2=0,module_3=0,module_4=0,auth_user=user)
        induccion.save()
    else:
        induccion = induccionaux[0]
    bandera = False
    if induccion.module_1>=5 and induccion.module_2>=5 and induccion.module_3>=5 and induccion.module_4>=4:
        bandera = True
    params = {"induccion":induccion,"usuario":request.user.username,"aprobado":bandera}
    return render(request,'sharedarea/induccion_intro.html',params)

def calendario(request):
    return render(request,'sharedarea/calendario.html')


def logout_user(request):
	if (request.user.is_authenticated()):
		logout(request)
	return redirect('/')

def induccion_modulo1(request):
    return render(request,'sharedarea/induccion_modulo1.html')

def induccion_modulo2(request):
    return render(request,'sharedarea/induccion_modulo2.html')

def induccion_modulo3(request):
    return render(request,'sharedarea/induccion_modulo3.html')

def induccion_modulo4(request):
    return render(request,'sharedarea/induccion_modulo4.html')

def test_modulo1(request):
    return render(request,'sharedarea/test_modulo1.html')

def test_modulo2(request):
    return render(request,'sharedarea/test_modulo2.html')

def test_modulo3(request):
    return render(request,'sharedarea/test_modulo3.html')

def test_modulo4(request):
    return render(request,'sharedarea/test_modulo4.html')

