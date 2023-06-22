from django.urls import path
from .views import EducationView, SkillView, ToolView, ProjectView, WorkHistoryView

# URLs for api endpoints
urlpatterns = [
    path('education', EducationView.as_view()),
    path('skill', SkillView.as_view()),
    path('tool', ToolView.as_view()),
    path('project', ProjectView.as_view()),
    path('work-history', WorkHistoryView.as_view()),
]