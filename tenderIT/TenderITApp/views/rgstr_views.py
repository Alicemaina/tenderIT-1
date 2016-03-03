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
		
		# Create the company object and save it to a database
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
   
    return render(request,'register.html',context)


def login(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['username']
            user = auth.authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/accounts/loggedin')
                else:
                    return HttpResponse('Disabled account')
            else:
                return redirect('/accounts/invalid')
    else:
        form = Login_form()
        context = {
            'form': form
        }
        return render(request, 'login.html', context )


def loggedin(request):
    context = {'full_name' : request.user.username}
    return render(request, 'loggedin.html', context)

def invalid_login(request):
    return render(request, 'invalid_login.html')


def logout(request):
    auth.logout(request)
    render(request, 'logout.html')

