from django import forms

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	author = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
	keywords = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	actual_file = forms.FileField()

class SearchForm(forms.Form):
	search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	author = forms.BooleanField(required=False)
	title = forms.BooleanField(required=False)
