from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from ..forms import Registration_form
from django.core.context_processors import csrf
from ..models import Company

def register_user(request):
    if request.method == 'POST':
        form = Registration_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    context = {
        'form' : Registration_form
    }
    context.update(csrf(request))
    return render(request, 'register.html', context)

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    context = {'full_name' : request.user.username}
    return render(request, 'loggedin.html', context)

def invalid_login(request):
    return render(request, 'invalid_login.html')


def logout(request):
    auth.logout(request)
    render(request, 'logout.html')

