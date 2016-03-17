from django import forms
from django.contrib.auth.models import User
from .models import (Company, Project)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div, Field

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

import datetime
from django.forms.extras.widgets import SelectDateWidget



# form used to register a new user
class UserForm(forms.ModelForm):
	username = forms.CharField(min_length = 4, max_length = 16, error_messages={'required': 'Please enter username.', 'min_length':'Username must have at least four charachters.'})

	password = forms.CharField(min_length = 4, max_length = 16, widget=forms.PasswordInput(), error_messages={'required': 'Please enter password.', 'min_length':'Password must have at least four charachters.'})
	
	class Meta:
 		model = User
		fields = ('username','password')

class CompanyForm(forms.ModelForm):
	website = forms.URLField(initial='http://', widget=forms.TextInput(attrs={'placeholder': 'Enter website...'}) )
	class Meta:
		model = Company

		fields = ('country', 'nationalID','name', 'street','city','postcode', 'email', 'phone', 'website')
		widgets = {'country':CountrySelectWidget()}
	def __init__(self, *args, **kwargs):
		super(CompanyForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.layout.append(Submit('save', 'save'))
		self.helper.layout = Layout(
			MultiField(


			)

		)


# form to add new project_templates
class Post_project(forms.ModelForm):
	title = forms.CharField(min_length=8, max_length=128, error_messages={'required': 'Please enter project title.', 'min_length':'Project title must contain at least eight charachters.'}, widget=forms.TextInput(attrs={'placeholder': 'Enter project title...', }))
	description = forms.CharField(min_length=32, max_length=2048, error_messages={'required': 'Please enter project description.', 'min_length':'Project description must contain at least 32 charachters.'}, widget=forms.Textarea(attrs={'placeholder': 'Enter project description...'}))
	budget = forms.IntegerField(min_value = 1, error_messages={'required': 'Please enter project budget.', 'min_value':'Projest budget cannot be less than one.'})
	startDate = forms.DateField(initial = datetime.datetime.now().date(),widget=SelectDateWidget)
	endDate =  forms.DateField(initial = datetime.datetime.now().date(),widget=SelectDateWidget)
	
	def clean(self):
		cleaned_data = super(Post_project, self).clean()
		startDate = cleaned_data.get('startDate')
		endDate = cleaned_data.get('endDate')		
		
		if startDate and endDate:
			# Check that start date is not in past
			if startDate <= datetime.datetime.now().date():
				msg = u'Start date cannot be in the past'
				self.add_error('startDate',msg)			

			# Check that end date is after start date
			if endDate <= startDate:
				msg = u'End date must be after start date.'
				self.add_error('endDate',msg)
		
		
		return cleaned_data

	class Meta:
		model = Project
		fields = ('title', 'description', 'budget', 'currency', 'startDate', 'endDate')
		


