from django.shortcuts import render, HttpResponseRedirect
from ..models import (Project,Company, ProjectApplication, Rating)
from ..forms import Post_project, Apply_project
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def index(request):
    c = {}
    return render(request, '../templates/index.html', c)

def project_view(request):
    lists = Project.objects.all()
    context = {
    'list': lists
     }
    return render(request, 'templates/project_view.html', context)

def company(request, company_id):
    context_dict = {}
    try:

	company = Company.objects.get(pk=company_id)
    	context_dict['company_templates'] = company

	context_dict['company'] = company

	projects = Project.objects.filter(company=company)
	context_dict['projects'] = projects
	
    except Company.DoesNotExist:
	pass
    
    return render(request, 'company_profile.html', context_dict)
	
def project(request, project_pk):
	context_dict = {}
	own_project = False
		
	try:
	 project = Project.objects.get(pk = project_pk)
	 if request.user.is_authenticated(): 
		company = Company.objects.get(user=request.user)
		if company == project.company:
			own_project = True
		try:
			apply_exist = ProjectApplication.objects.get(applicant=company, project=project)
		except ProjectApplication.DoesNotExist:
			apply_exist = None
<<<<<<< HEAD

=======
		applications = ProjectApplication.objects.filter(project=project)
	 context_dict['applications'] = applications	
>>>>>>> 44fd741cb8d9e7c90e90ad0c6b10c2040cabb228
	 context_dict['project'] = project
	 context_dict['own_project'] = own_project
	 context_dict['apply_exist'] = apply_exist
	except Project.DoesNotExist:
	 pass
	
	return render(request, 'project_view.html', context_dict)


@login_required
def post_project(request):
	project_added = False
   	if request.method == 'POST':
		project_form = Post_project(request.POST, request.FILES)
        	if project_form.is_valid():
				project=project_form.save(commit=False)
				project.company = Company.objects.get(user=request.user)
				project.save()
				project_added=True				               
	else:
         project_form = Post_project()

	context = {
        'form' : project_form,
		'project_added' : project_added
    }
	return render(request, 'new_project.html', context)

@login_required
def project_edit(request, project_pk):
	project = get_object_or_404(Project, pk = project_pk)
	if request.method == 'POST':
		project_form = Post_project(request.POST, instance = project)
		if project_form.is_valid():
			project = project_form.save()
	else:
		project_form = Post_project(instance=project)
	context = {'form': project_form,}
	return render(request, 'new_project.html', context)
			
    
def companies(request):
    company_list = Company.objects.order_by('name')	
    context_dict = {'companies' : company_list}

    return render(request, 'companies.html', context_dict)

def projects(request):
	project_list = Project.objects.order_by('publishDate')
	context_dict = {'projects' : project_list}
	
	return render(request, 'projects.html', context_dict)

@login_required
def my_projects(request):
	project_list = Project.objects.filter(company=request.user.company)
	context_dict = {'projects' : project_list}
	return render(request, 'projects.html', context_dict)

@login_required
def my_applications(request):
	application_list = ProjectApplication.objects.filter(applicant=request.user.company)
	context_dict = {'applications' : application_list}
	return render(request, 'applications.html', context_dict)

@login_required
def apply_project(request, project_id):
	application_added = False
	project	= Project.objects.get(id=project_id)
   	if request.method == 'POST':
		apply_form = Apply_project(request.POST)
        	if apply_form.is_valid():
				application = apply_form.save(commit=False)
				application.project = Project.objects.get(id=project_id)
				application.applicant = Company.objects.get(user=request.user)
				application.save()				
				application_added=True	
				project = application.project	
	               
	    	else:
				print apply_form.errors
	else:
         	apply_form = Apply_project()

	context = {
        'form' : apply_form,
	'application_added' : application_added,
	'project' : project,
	
    }
	return render(request, 'application.html', context)

@login_required
def application_edit(request, application_id):
	application = get_object_or_404(ProjectApplication, pk = application_id)
	project = application.project
	if request.method == 'POST':
		apply_form = Apply_project(request.POST, instance = application)
		if apply_form.is_valid():
			application = apply_form.save()
	else:
		apply_form = Apply_project(instance=application)
	context = {'form': apply_form,
		'project': project,
		}
	return render(request, 'application.html', context)

@login_required
def rate_project(request, project_id):

     ## Almin as we discussed before you can write this method if you want
    return 


