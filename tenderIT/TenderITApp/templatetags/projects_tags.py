from django import template
register = template.Library()
from ..models import Project

@register.simple_tag
def project_count():
    Project.objects.count()
    


@register.assignment_tag
def show_latest_projects(count = 8):
    latest_projects = Project.objects.order_by('-publishDate')[:count]
    return latest_projects


