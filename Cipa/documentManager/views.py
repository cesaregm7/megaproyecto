# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.shortcuts import render, redirect
from .forms import UploadFileForm, SearchForm
from django.http import HttpResponseRedirect, HttpResponse
from sharedarea.models import *

from django.db.models import Q 
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils.encoding import smart_str

import string
import random
import os

from django.conf import settings

# Create your views here.



def get_id(size=8, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def handle_uploaded_file(request, form):
	base_link = settings.MEDIA_ROOT + "/uploaded_documents/"
	base_unused = "//home/ubuntu/Cipa"


	#Guardar archivo
	uploaded_file = request.FILES['actual_file']
	path = default_storage.save(base_link + uploaded_file.name.encode('ascii', 'ignore'), ContentFile(uploaded_file.read()))

	path = path[len(base_unused):]

	#Obtener usuario
	user = AuthUser.objects.filter(username = request.user.username)[0]

	#Guardarlo en BD
	new_file = Documents()
	new_file.author = form.cleaned_data['author']
	new_file.link = "/" + path
	new_file.keywords = form.cleaned_data['keywords']
	new_file.title = form.cleaned_data['title']
	new_file.uploaded_by = user

	new_file.save()

	return new_file
#Guardar modelo aqui

@login_required
def subir_documento(request):
	#Verificar permisos
	if not (request.user.groups.filter(name='Administrador').exists()
		or  request.user.groups.filter(name='Catedrático').exists()):
		return redirect('/herramientas')
	 #Entrada por POST
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		#Validar formulario
		if form.is_valid():
			#Guardar documento
			new_file = handle_uploaded_file(request, form)
			return render(request,'sharedarea/documentManager/index_successfull_upload.html', {'new_file': new_file})
		else:
			return render(request,'sharedarea/documentManager/index_upload.html', {'form': form})
	#Entrada por GET
	form = UploadFileForm()
	return render(request,'sharedarea/documentManager/index_upload.html', {'form': form})

@login_required
def ver_busqueda_documento(request, search):
	form = SearchForm(request.POST or None)
	search_list = None

	if form.is_valid():
		search_list = form.cleaned_data['search'].split(" ")
		search_author = form.cleaned_data['author']
		search_title = form.cleaned_data['title']
	elif len(search) > 0 and not form.is_valid():
		search_list = search.split(" ")
		search_author = True
		search_title = True

		form.fields['search'].initial = search
	if not search_list is None:
		q_objects = Q()

		if search_author == search_title:
			for search_item in search_list:
				q_objects |= Q(author__icontains = search_item)
				q_objects |= Q(title__icontains = search_item)
				q_objects |= Q(keywords__icontains = search_item)
		elif search_author == True:
			for search_item in search_list:
				q_objects |= Q(author__icontains = search_item)
				q_objects |= Q(keywords__icontains = search_item)
		elif search_title == True:
			for search_item in search_list:
				q_objects |= Q(title__icontains = search_item)
				q_objects |= Q(keywords__icontains = search_item)

		docs = Documents.objects.filter(q_objects)
			
		#Mostrar resultados de busqueda
		return render(request,'sharedarea/documentManager/index_doc_search.html', {'search_form' : form,'docs' : docs})		
	#mostrar ultimos 10 docs
	docs = Documents.objects.all().order_by('-id_documents')[:10]
	return render(request,'sharedarea/documentManager/index_doc_search.html', {'search_form' : form,'docs' : docs})

@login_required
def recomendaciones(request):
	test_from = -1
	if request.method == "POST":
		test_from = int(request.POST["preselect"])

	tests = Test.objects.all()
	test_recomendations = []
	preselect = -1

	for test in tests:
		recomendations = Recomendation.objects.filter(id_test_recomendation=test.id_test)
		if recomendations.count() > 0:
			test_recomendations.append([test, recomendations, test.id_test])
			if test.id_test == test_from:
				preselect = len(test_recomendations) - 1

	params = {'recom_list' : test_recomendations, 'preselect' : preselect}

	return render(request,'sharedarea/documentManager/index_recomendaciones.html', params)


