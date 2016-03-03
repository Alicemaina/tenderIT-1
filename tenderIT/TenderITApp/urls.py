from django.conf.urls import patterns, url

from .views import (content_views, rgstr_views)

urlpatterns = patterns('',
    url(r'^$', content_views.index, name="index"),
    url(r'^project_view/$', content_views.project_view, name="project_view"),
    url(r'^(?P<company_id>[0-9]+)/$', content_views.company, name="company"),
    url(r'^register/$', rgstr_views.register_user, name="register"),
    url(r'^login/$', rgstr_views.login, name="login"),
   ##  url(r'^company'),
    url(r'^logout/$', rgstr_views.logout, name="logout"),
    url(r'^auth/$', rgstr_views.auth_view, name="auth"),
    url(r'^post_project/$', content_views.post_project, name="post_project "),
    url(r'^(?P<project_id>[0-9]+)/$', content_views.apply_project, name="apply_project"),

)
