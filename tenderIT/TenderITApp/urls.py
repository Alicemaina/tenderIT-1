from django.conf.urls import url
from django.conf import  settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import (login, logout, password_change, password_change_done, password_reset, password_reset_done, password_reset_confirm, password_reset_complete)
from .views import (content_views, rgstr_views)


# content related urls
urlpatterns = [
    url(r'^$', content_views.index, name="index"),
    url(r'^company/(?P<company_id>[\w\-]+)/$', content_views.company, name="company"),
	url(r'^project/(?P<project_pk>[\w\-]+)/$', content_views.project, name="project"),
	url(r'^project/(?P<project_pk>[\w\-]+)/edit/$', content_views.project_edit, name="project-edit"),
    url(r'^project/(?P<project_pk>[\w\-]+)/delete/$',content_views.delete_project, name="delete-project"),
    url(r'^projects/all/$', content_views.project_list, name="projects"),
    url(r'^companies/$', content_views.companies, name="companies"),
    url(r'^post_project/$', content_views.post_project, name="post_project"),
    url(r'^project/(?P<project_id>[0-9]+)/apply/$', content_views.apply_project, name="apply_project"),
	url(r'^my_projects/$', content_views.my_projects, name="my_projects"),
	url(r'^my_applications/$', content_views.my_applications, name="my_applications"),
	url(r'^my_applications/(?P<application_id>[0-9]+)/edit/$', content_views.application_edit, name="application_edit"),
    url(r'^update_decription/(?P<company_id>[\w\-]+)/$', content_views.update_company_desc, name="update"),
    url(r'^search/$', content_views.search, name='search')
	]

# account related urls
urlpatterns += (
    url(r'^register/$', rgstr_views.register_user, name="register"),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name="login"),
    url(r'^logged_in/$', rgstr_views.logged_in, name="logged_in"),
    url(r'^logout/$', logout,{'template_name': 'registration/log_out.html'}, name="logout"),
    url(r'^password-change/$', password_change,
        {'template_name': 'registration/password_change.html'}, name='password_change'),
    url(r'^password_change/done/$', password_change_done,
        {'template_name': 'registration/password_change_done.html'}, name='password_change_done'),
    url(r'^password-reset/$', password_reset,
        {'template_name': 'registration/password_reset.html'}, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done,
        {'template_name': 'registration/password_rst_done.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm, {'template_name': 'registration/password_rst_confirm.html'}, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete,
        {'template_name': 'registration/password_rst_complete.html'}, name='password_reset_complete')
    )

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
