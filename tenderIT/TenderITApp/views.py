from django.http import HttpResponse
from django.contrib import auth
from TenderITApp.forms import UserForm, CompanyForm, Login_form, Post_project
from django.core.context_processors import csrf
from django.shortcuts import render, HttpResponseRedirect, redirect
from TenderITApp.models import (Project,Company, ProjectApplication, Rating)
from django.contrib.auth.decorators import login_required

def index(request):
    c = {}
    return render(request, 'tenderit/index.html', c)

def project_view(request):
    lists = Project.objects.all()
    context = {
    'list': lists
     }
    return render(request, 'tenderit/project_view.html', context)

def company(request, company_id):
    context_dict = {}
    try:
	company = Company.objects.get(nationalID=company_id)
    	context_dict['company'] = company
	projects = Project.objects.filter(company=company)
	context_dict['projects'] = projects
	
    except Company.DoesNotExist:
	pass
    
    return render(request, 'tenderit/company_profile.html', context_dict)
	
def project(request, project_pk):
	context_dict = {}
	try:
	 project = Project.objects.get(pk = project_pk)
	 context_dict['project'] = project
	except Project.DoesNotExist:
	 pass
	
	return render(request, 'tenderit/project_view.html', context_dict)


@login_required
def post_project(request):
    if request.user.is_authenticated():
        if request.POST:
            form = Post_project
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/projects/all')
    else:
        return HttpResponseRedirect('/login')

    context = {
        'form' : Post_project
    }
    return render(request, 'tenderit/new_project.html', context)

def companies(request):
    company_list = Company.objects.order_by('name')	
    context_dict = {'companies' : company_list}

    return render(request, 'tenderit/companies.html', context_dict)

@login_required
def apply_project(request, project_id):

    if request.user.is_authenticated():
        if request.POST:
            price = request.get.POST('price', '')
            description = request.get.POST('description', '')
            application = ProjectApplication(Project = project_id, applicant = request.user,
                                             price = price, description = description)

    else:
        return HttpResponseRedirect('login.html')
    project = Project.objects.get(pk = project_id)
    context = {
        'projects' : project
    }
    return render(request, 'tenderit/apply.html', context)

@login_required
def rate_project(request, project_id):

     ## Almin as we discussed before you can write this method if you want
    return ()

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
   
    return render(request,'/tenderit/registration/register.html',context)



def logged_in(request):
	user = request.user
	company = user.company
	company_id = user.company.pk
	return redirect('tenderit/company/%d/' %company_id,{'company':company})

