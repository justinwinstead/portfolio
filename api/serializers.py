from rest_framework import serializers
from .models import Education, Skill, Tool, Project, WorkHistory

class EducationSerializer(serializers.ModelSerializer):
    '''
    class to serialize Education model to JSON
    '''
    class Meta:
        model = Education
        fields = (
            'id',
            'institution',
            'credential',
            'major',
            'gpa',
            'coursework'
        )

class SkillSerializer(serializers.ModelSerializer):
    '''
    class to serialize Skill model to JSON
    '''
    class Meta:
        model = Skill
        fields = (
            'id',
            'description',
            'proficiency',
            'duration'
        )

class ToolSerializer(serializers.ModelSerializer):
    '''
    class to serialize Tool model to JSON
    '''
    class Meta:
        model = Tool
        fields = (
            'id',
            'name',
            'category',
            'proficiency',
            'duration'
        )

class ProjectSerializer(serializers.ModelSerializer):
    '''
    class to serialize Project model to JSON
    '''
    class Meta:
        model = Project
        fields = (
            'id',
            'description',
            'languages',
            'url'
        )

class WorkHistorySerializer(serializers.ModelSerializer):
    '''
    class to serialize WorkHistory model to JSON
    '''
    class Meta:
        model = WorkHistory
        fields = (
            'id',
            'employer',
            'location',
            'start_date',
            'end_date',
            'responsibilities'
        )