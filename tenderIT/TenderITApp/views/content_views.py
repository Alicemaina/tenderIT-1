from django.shortcuts import render, HttpResponseRedirect
from tenderIT.TenderITApp.models import (Project,Company, ProjectApplication, Rating)
from tenderIT.TenderITApp.forms import Post_project
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
    return render(request, 'new_project.html', context)


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


def rate_project(request, project_id):

        ## I will implement this with ajax
    return ()
