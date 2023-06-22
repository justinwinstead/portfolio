from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Education, Skill, Tool, Project, WorkHistory
from .serializers import EducationSerializer, SkillSerializer, ToolSerializer, ProjectSerializer, WorkHistorySerializer

class EducationView(generics.ListAPIView):
    '''
    view that allows database query for Education objects

      attributes:
        queryset: contains all Education objects in the database
        serializer_class: a class to serialize Education objects into JSON
    '''
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class SkillView(generics.ListAPIView):
    '''
    view that allows database query for Skill objects

      attributes:
        queryset: contains all Skill objects in the database
        serializer_class: a class to serialize Skill objects into JSON
    '''
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ToolView(APIView):
    '''
    view that allows database query for Tool objects

      attributes:
        serializer_class: a class to serialize Tool objects into JSON
        lookup_url_kwarg: the name of the variable provided in HTTP request from React

      functions:
        get(): returns the tools for a provided category
    '''
    serializer_class = ToolSerializer
    lookup_url_kwarg = 'category'

    def get(self, request, format=None):
        category = request.GET.get(self.lookup_url_kwarg)

        if category is not None:
            tools = Tool.objects.filter(category=category)

            # return Tool data if it exists
            if len(tools):
                data = []
                for tool in tools:
                    data.append(ToolSerializer(tool).data)
          
                return Response(data, status=status.HTTP_200_OK)
            
            # return 404 message if category does not exist
            return Response({'Tools not found': 'Invalid category choice'}, status=status.HTTP_404_NOT_FOUND)       

        # return 400 message if category parameter is not in request
        return Response({'Bad Request': 'Category parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)         


class ProjectView(generics.ListAPIView):
    '''
    view that allows database query for Project objects

      attributes:
        queryset: contains all Project objects in the database
        serializer_class: a class to serialize Project objects into JSON
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class WorkHistoryView(generics.ListAPIView):
    '''
    view that allows database query for WorkHistory objects

      attributes:
        queryset: contains all WorkHistory objects in the database
        serializer_class: a class to serialize WorkHistory objects into JSON
    '''
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer

