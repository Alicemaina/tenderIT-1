from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from ..forms import UserForm, CompanyForm, Login_form

from django.core.context_processors import csrf
from ..models import Company


def register_user(request):
    # A boolean value for telling the template whether the registration was successful.  
    registered = False
    if request.method == 'POST':
	
	# Take information from forms
	user_form = UserForm(data=request.POST)
	company_form = CompanyForm(data=request.POST)

	# If two forms are valid...
	if user_form.is_valid() and company_form.is_valid():
		#Save the user's form data to the database.
		user = user_form.save()
		# Hash the password with the set_password method and update the user Object.              
		user.set_password(user.password)
		user.save()
		
		# Create the company_templates object and save it to a database
		company = company_form.save(commit=False)
		company.user = user
		company.save()
	
		# Update boolean value
		registered = True
	
	# Forms not valid, print errors	
	else:
		print user_form.errors, company_form.errors

     # Not POST, show forms
    else:
	user_form = UserForm()
	company_form = CompanyForm()        
      
    context = {'user_form' : user_form,
	       'company_form' : company_form,
	       'registered': registered,}
   
    return render(request,'registration/register.html',context)



def logged_in(request):
	user = request.user
	company = user.company
	company_id = user.company.pk
	return redirect('/company/%d/' %company_id,{'company':company})


