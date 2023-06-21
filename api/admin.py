from django.contrib import admin

from .models import Education, Skill, Tool, Project, WorkHistory

# register the models to the Django admin interface
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Tool)
admin.site.register(Project)
admin.site.register(WorkHistory)