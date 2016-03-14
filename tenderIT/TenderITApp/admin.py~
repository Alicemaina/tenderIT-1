from django.contrib import admin
from TenderITApp.models import Company, Project, Rating, ProjectApplication

class CompanyAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Company, CompanyAdmin)
admin.site.register(Project)
admin.site.register(Rating)
admin.site.register(ProjectApplication)


