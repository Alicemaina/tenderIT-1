from django.shortcuts import render, HttpResponseRedirect
from ..models import (Project,Company, ProjectApplication, Rating)
from ..forms import Post_project
from django.contrib.auth.decorators import login_required


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
	try:
	 project = Project.objects.get(pk = project_pk)
	 context_dict['project'] = project
	except Project.DoesNotExist:
	 pass
	
	return render(request, 'project_view.html', context_dict)


@login_required
def post_project(request):
	project_added = False
   	if request.method == 'POST':
		project_form = Post_project(request.POST)
        	if project_form.is_valid():
				project=project_form.save(commit=False)
				project.company = Company.objects.get(user=request.user)
				project.save()
				project_added=True				               
	    	else:
				print project_form.errors
	else:
         project_form = Post_project()

	context = {
        'form' : project_form,
		'project_added' : project_added
    }
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
    return render(request, 'apply.html', context)

@login_required
def rate_project(request, project_id):

     ## Almin as we discussed before you can write this method if you want
    return 
