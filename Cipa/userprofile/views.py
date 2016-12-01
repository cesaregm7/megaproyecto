# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib.auth.models import User, Group

# Create your views here.

from easy_pdf.views import PDFTemplateView
import easy_pdf


def pdf_template(request, pk):
	if (not request.user.is_authenticated()):
		return redirect('/')
	if not (request.user.groups.filter(name='Administrador').exists() or request.user.groups.filter(name='Catedrático').exists()):
		return redirect('/herramientas')
	usuario= get_object_or_404(AuthUser, pk=pk)
	skills = get_object_or_404(UserSkills, auth_user=usuario)
	formUser = UserDataForm(request.POST or None, instance=usuario)
	formSkills = UserSkillForm(request.POST or None, instance=skills)
	return easy_pdf.rendering.render_to_pdf_response(request, 'sharedarea/pdf_template.html', {'formUser': formUser, 'formSkills': formSkills}, filename=None, encoding='utf-8')

def list_user_profiles(request):
	if (not request.user.is_authenticated()):
		return redirect('/')
	if not (request.user.groups.filter(name='Administrador').exists() or request.user.groups.filter(name='Catedrático').exists()):
		return redirect('/herramientas')
	student_ids = User.objects.filter(groups__name='Estudiante')
	usuarios = AuthUser.objects.filter(id__in=student_ids).exclude(first_name='')
	data = {}
	data['object_list'] = usuarios
	return render(request, 'sharedarea/list_user_profiles.html', data)

def update_user_profile(request, pk):
	if (not request.user.is_authenticated()):
		return redirect('/')
	if int(request.user.id) != int(pk):
		return redirect('/herramientas')

	usuario = get_object_or_404(AuthUser, pk=pk)
	skills, created = UserSkills.objects.get_or_create(auth_user= usuario)

	if(created):
		formUser = UserDataForm(request.POST or None, request.FILES or None, instance=usuario)
		formSkills = UserSkillForm(request.POST or None, instance=skills)
		if formUser.is_valid() and formSkills.is_valid():
			formUser.save()
			formSkills.save()
			return render(request, 'sharedarea/herramientas.html', {'formUser': formUser, 'formSkills': formSkills})
		return render(request, 'sharedarea/user_profile.html', {'formUser': formUser, 'formSkills': formSkills})
	else:
		formUser = UserDataForm(request.POST or None, request.FILES or None, instance=usuario)
		formSkills = UserSkillForm(request.POST or None, instance=skills)
		if formUser.is_valid() and formSkills.is_valid():
			formUser.save()
			formSkills.save()
			return render(request, 'sharedarea/herramientas.html', {'formUser': formUser, 'formSkills': formSkills})
		return render(request, 'sharedarea/user_profile.html', {'formUser': formUser, 'formSkills': formSkills})
def view_user_profile(request, pk):
	if (not request.user.is_authenticated()):
		return redirect('/')
	if not (request.user.groups.filter(name='Administrador').exists() or request.user.groups.filter(name='Catedrático').exists()):
		return redirect('/herramientas')
	usuario= get_object_or_404(AuthUser, pk=pk)
	skills, created = UserSkills.objects.get_or_create(auth_user= usuario)

	if(created):
		formUser = UserDataForm(request.POST or None, instance=usuario)
		formSkills = UserSkillForm(request.POST or None)
	else:
		formUser = UserDataForm(request.POST or None, instance=usuario)
		formSkills = UserSkillForm(request.POST or None, instance=skills)


	return render(request, 'sharedarea/view_user_profile.html', {'formUser': formUser, 'formSkills': formSkills, 'id':pk})



