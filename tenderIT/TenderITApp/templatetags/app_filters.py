from django import template
register = template.Library()
from ..models import Project


# # @register.filter(name="is_own_project"):
# def check_project_owner(project_id):
#
#
