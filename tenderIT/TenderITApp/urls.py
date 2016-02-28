from django.conf.urls import url, patterns

from . import views

urlpatterns = [

    url(r'^project_view/$', views.project_view, name="project_view"),
    url(r'^(?P<company_id>[0-9]+)/$', views.company, name="company"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login /$', views.login , name="login "),
    url(r'^post_project /$', views.post_project , name="post_project "),
    url(r'^(?P<project_id>[0-9]+)/$', views.apply_project, name="apply_project"),

]
