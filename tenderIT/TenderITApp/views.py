
from django.shortcuts import render, HttpResponseRedirect
from .models import Project
from .models import Company
# Create your views here.

def project_view(request):
    lists = Project.objects.all()
    context = {
    'list': lists
     }
    return render(request, 'templates/project_view.html', context)

def company(request, company_id):
    company = Company.objects.get(pk = company_id)
    context = {
    'company': company
    }
    return (request, 'templates/company_profile', context)


def register(request):
    if request.POST:
        company = Company(name = request.POST('name'),username = request.POST('username'), email = request.POST('email'),
                          password = request.POST('password'))
        company.save()
        return HttpResponseRedirect(request, 'templates/company_details.html', {})
    else:
        return (request, 'templates/register.html', {})


def login(request):
    if request.POST:
        # will be some validations
        # don't worry about anythig yet
        return HttpResponseRedirect(request, 'templates/company_profile.html')
    else:
        return (request, 'templates/login.html', {})


def post_project(request):
    if request.POST:
        # also some validations for project details here
        project = Project(title = request.POST('title'),description = request.POST('description'), budget = request.POST('budget'),
                          currency = request.POST('currency'), startdate = request.POST('startdate'),)
        project.save()
        return HttpResponseRedirect(request, '', {})

def apply_project(request, project_id):
    project = Project.objects.get(pk = project_id)
    render(request, 'templates.project.html', {})
