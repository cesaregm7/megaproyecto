# -*- coding: utf-8 -*-
from django import forms
from sharedarea.models import *

class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
	return obj.first_name + " " +obj.last_name

