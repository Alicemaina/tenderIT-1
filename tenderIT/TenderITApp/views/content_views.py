from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from ..models import (Project,Company, ProjectApplication, Rating, )
from django.db.models import Q
from ..forms import Post_project, Apply_project, Edit_project
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Home page view
def index(request):
	c = {}
	return render(request, 'index.html', c)

# All companies view, handels request for all companies, orders companies by name
def companies(request):
	company_list = Company.objects.order_by('name')	
	context_dict = {'companies' : company_list}
	return render(request, 'companies.html', context_dict)

# Single company view, handles request for a company based on company id (primary key)
def company(request, company_id):

	own_profile = False
	user = request.user

	company = get_object_or_404(Company, pk=company_id)
	if user.is_authenticated:
		try:
			if user.company:
				if user.company.pk == company.pk:
					own_profile = True
		except Exception:
			pass
	context_dict = {}
	application_list = ProjectApplication.objects.filter(applicant=company)

	# Get company by company id
	context_dict['company'] = company
	projects = Project.objects.filter(company=company)
	# Get company projects
	context_dict = {}
	try:
		context_dict['applications']= application_list
		# context_dict['own_profile'] = own_profile
		company = Company.objects.get(pk=company_id) 		# Get company by company id
		context_dict['company'] = company		
		projects = Project.objects.filter(company=company)  # Get company projects
		context_dict['projects'] = projects	
	# Company does not exist, do nothing
	except Company.DoesNotExist:
		pass

	return render(request, 'company_profile.html', context_dict)


# All projects view, handels request for all projects, orders projects by publish date.
def projects(request):
	project_list = Project.objects.order_by('publishDate')
	context_dict = {'projects' : project_list}	
	return render(request, 'projects.html', context_dict)

	projects = Project.objects.filter(company=company)
	context_dict['projects'] = projects

	return render(request, 'company_profile.html', context_dict)


# Single project view, handles request for a project based on projects primary key

def project(request, project_pk):
	context_dict = {}
	own_project = False
	apply_exist = None
	# Variable to show does the project belong to authenticated user
	try:	
		project = Project.objects.get(pk = project_pk)  # Get project by primary key
	 
	 # If user is authenticated check is he the owner of the project and check did he already applied for this project

		if request.user.is_authenticated():
			company = Company.objects.get(user=request.user)
			if company == project.company:
				own_project = True

			try:
				apply_exist = ProjectApplication.objects.get(applicant=company, project=project)
			except ProjectApplication.DoesNotExist:
				apply_exist = None

			# Get project application for this project


		# Get project application for this project
		applications = ProjectApplication.objects.filter(project=project)
		context_dict['applications'] = applications
		context_dict['project'] = project
		context_dict['own_project'] = own_project
		context_dict['apply_exist'] = apply_exist
	# Project does not exist, do nothing

	except Project.DoesNotExist:
		pass
	
	return render(request, 'project_templates/project.html', context_dict)

# Publish new project, user must be authenticated to publish projects
@login_required
def post_project(request):
	project_added = False  # Value to tell the template is the project added.

	# If request is POST check form validity and create new project object
	if request.method == 'POST':
		project_form = Post_project(request.POST, request.FILES)
		if project_form.is_valid():
			project=project_form.save(commit=False)
			project.company = Company.objects.get(user=request.user)
			project.avatar = request.FILES['avatar']
			project.document = request.FILES['document']
			project.save()
			project_added=True	
	# Request not POST, show the form			               
	else:
		project_form = Post_project()

	context = {
        'form' : project_form,
		'project_added' : project_added
    }
	return render(request, 'project_templates/new_project.html', context)

# updates company description
def update_company_desc(request, company_id):
	if request.method == 'POST':
		company = get_object_or_404(Company, pk= company_id)
		new_description = request.POST.get('hiddeninput')
		company.description = new_description
		company.save(update_fields = ["description"])
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




@login_required
def project_edit(request, project_pk):
	project = get_object_or_404(Project, pk = project_pk)
	if request.method == 'POST':
		project_form = Edit_project(request.POST, request.FILES)

		if project_form.is_valid():
			project.budget = request.POST.get('budget', '')
			project.title = request.POST.get('title','')
			project.description = request.POST.get('description','')
			project.startDate = request.POST.get('startDate','')
			project.endDate = request.POST.get('endDate','')
			project.avatar = request.FILES['avatar']
			project.document = request.FILES['document']
			project.save(update_fields= ['budget', 'title', 'description', 'startDate', 'endDate', 'avatar', 'document'])
	else:
		project_form = Post_project(instance=project)
		context = {'form': project_form,}
	return render(request, 'project_templates/edit_project.html', context)


# deletes a project
def delete_project(request, project_pk):
	project = get_object_or_404(Project, pk = project_pk)
	if request.method == 'POST':
		project.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# Show authenticated user projects, uses the same template as for all projects    
@login_required
def my_projects(request):
	project_list = Project.objects.filter(company=request.user.company)
	context_dict = {'projects' : project_list}
	return render(request, 'projects.html', context_dict)



# Show authenticated user project applications
@login_required
def my_applications(request):
	application_list = ProjectApplication.objects.filter(applicant=request.user.company)
	context_dict = {'applications' : application_list}
	return render(request, 'applications.html', context_dict)



# Apply project view, user must be authenticated to apply for projects
@login_required
def apply_project(request, project_id):
	print project_id
	application_added = False # Value to tell the template whether the application was sucessfull
	project	= Project.objects.get(id=project_id) # Get project by project id
	# If request is POST check form validity and create new ProjectApplication
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
	# Request not POST, show the form
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



 # Left for better days.
@login_required
def rate_project(request, project_id):   
	return 

# get list of projects
def project_list(request):
	context_dict ={}
	projects_list = Project.objects.all().order_by('title')
	print projects_list

	context_dict['projects_list']= projects_list
	return render(request, "project_templates/projects.html", context_dict)

# search view
def search(request):
	context = {}
	if request.method == 'POST':
		q =request.POST.get('search-item')
		print q

		companies = Company.objects.filter(Q(name__icontains= q)| Q(country__icontains= q )| Q(city__icontains= q)|Q(email__icontains= q)|
										   Q(street__icontains= q)|Q(website__icontains= q)).order_by('name')
		projects = Project.objects.filter(Q(title__icontains= q))

		context ={
			'companies': companies,
			'projects': projects
		}

	return render(request, 'search.html', context)
