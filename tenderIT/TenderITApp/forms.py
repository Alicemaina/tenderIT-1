from django import forms
from django.contrib.auth.models import User
from .models import (Company, Project)


# form used to register a new user
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username','password')

class CompanyForm(forms.ModelForm):
	
	website = forms.URLField(max_length=200, help_text="Please enter the URL of the page.", initial='http://')

	class Meta:
		model = Company
		fields = ('name', 'nationalID', 'street','city','country','postcode', 'email', 'phone', 'website')	


# form to add new project
class Post_project(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'budget', 'currency', 'startDate', 'endDate', 'documents', 'slug')

