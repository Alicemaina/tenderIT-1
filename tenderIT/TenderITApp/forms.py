from django import forms
from django.contrib.auth.models import User

from .models import (Company, Project)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div, Field
from crispy_forms.bootstrap import AppendedText

from .models import (Company, Project, ProjectApplication)

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
	description = forms.CharField(min_length=32, max_length=2048, error_messages={'required': 'Please enter project description.', 'min_length':'Project description must contain at least 32 charachters.'}, widget=forms.Textarea(attrs={'placeholder': 'Enter project description...','rows': 6, 'cols': 10}))
	budget = forms.IntegerField(min_value = 1, error_messages={'required': 'Please enter project budget.', 'min_value':'Projest budget cannot be less than one.'})
	startDate = forms.DateField(initial = datetime.datetime.now().date())
	endDate =  forms.DateField(initial = datetime.datetime.now().date())
	
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

	def __init__(self, *args, **kwargs):
		super(Post_project, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_class= 'form-horizontal'
		self.helper.label_class= 'project_label col-lg-3 project_container'
		self.helper.field_class= 'project_field col-lg-8 project_container'
		self.helper.layout = Layout(
			Div(
				Field('title', wrapper_class="project_jumbo jumbotron row project_container", css_class="project_container" ,),
				Field('description', wrapper_class="description project_jumbo jumbotron row project_container", css_class="vresize"),
				Field('budget', wrapper_class="project_jumbo jumbotron row project_container", css_class="project_container"),
				Field('currency', wrapper_class="project_jumbo jumbotron row project_container", css_class="project_container"),
				css_class= "project_container col-lg-5 col-lg-offset-1 col-md-6 "
			),

			Div(
				Field('startDate', wrapper_class="project_jumbo jumbotron row project_container", css_class="project_container"),
				Field('endDate', wrapper_class="project_jumbo jumbotron row project_container",css_class="project_container"),

				Submit('Post Project', 'Postproject', css_class="greenbtn btn-block project_container"),
				css_class= "project_container col-lg-4 col-lg-offset-1 col-md-4 col-md-offset-1"


			),

		)



	class Meta:
		model = Project
		fields = ('title', 'description', 'budget', 'currency', 'startDate', 'endDate')


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



