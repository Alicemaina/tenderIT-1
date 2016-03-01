from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import (Company, Project)


# form used to register a new user
class Registration_form(UserCreationForm):
    class Meta:
        model = Company
        fields = ('name', 'username', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user = super(Registration_form, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# form to add new project

class Post_project(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'budget', 'currency', 'startDate', 'endDate', 'documents', 'slug')

