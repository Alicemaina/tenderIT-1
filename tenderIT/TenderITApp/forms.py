from django import forms
from django.contrib.auth.models import User
<<<<<<< HEAD
from .models import (Company, Project)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div, Field
=======
from .models import (Company, Project, ProjectApplication)
>>>>>>> 27ad52eb056c3c1a06cf2735939286219a2f67a2

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

import datetime
from django.forms.extras.widgets import SelectDateWidget



# form used to register a new user
class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
	password = forms.CharField(widget=forms.PasswordInput(render_value= False, attrs={'placeholder':'Enter your password'}))
	class Meta:
 		model = User
		widgets = {
			'password': forms.PasswordInput
		}
		fields = ('username','password')

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.layout.append(Submit('Register', 'Register', css_class='registerbtn btn-block'))
		self.helper.form_show_labels= False
		self.helper.render_required_fields = True


class CompanyForm(forms.ModelForm):
	website = forms.URLField(initial='http://', widget=forms.TextInput(attrs={'placeholder': 'Enter website...'}) )
	class Meta:
		model = Company

		fields = ('country', 'nationalID','name', 'street','city','postcode', 'email', 'phone', 'website')
		widgets = {'country':CountrySelectWidget()}
	def __init__(self, *args, **kwargs):
		super(CompanyForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		# self.helper.form_show_labels= False
		self.helper.form_class= 'form-horizontal form-group'
		self.helper.labels_uppercase= True



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
<<<<<<< HEAD
		
=======

# Apply for a project		
class Apply_project(forms.ModelForm):
	price = forms.IntegerField(min_value = 1, error_messages={'required': 'Please enter offered price.', 'min_value':'Price cannot be less than one.'})
	description = forms.CharField(min_length=32, max_length=2048, error_messages={'required': 'Please enter project description.', 'min_length':'Project description must contain at least 32 charachters.'}, widget=forms.Textarea(attrs={'placeholder': 'Enter project description...'}))

	class Meta:
		model = ProjectApplication
		fields = ('price','description')


class Login_form(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

>>>>>>> 27ad52eb056c3c1a06cf2735939286219a2f67a2
