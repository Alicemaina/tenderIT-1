from django import template
register = template.Library()
from ..models import Project

@register.simple_tag
def project_count():
    Project.objects.count()
    


@register.inclusion_tag('project_templates/latest_projects.html')
def latest_projets(count = 5):
    latest_projects = Project.objects.order_by('-publish')[:count]
    return {'latest_projects': latest_projects}

