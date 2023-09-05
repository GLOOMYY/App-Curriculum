from rest_framework import generics, authentication, permissions, filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Stack, ProjectDev, EmploymentHistory, Academy, HobbiesExtras, Skills, Facts
from .serializers import StackSerializer, ProjectDevSerializer, EmploymentHistorySerializer, AcademySerializer, HobbiesExtrasSerializer, SkillsSerializer, FactsSerializer

# Create your views here.

class StackListView(generics.ListAPIView):
  queryset = Stack.objects.all()
  serializer_class = StackSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['name_stack']
  # authentication_class = [authentication.TokenAuthentication]



class StackCreateView(generics.CreateAPIView):
  serializer_class = StackSerializer


class StackUpdateView(generics.RetrieveUpdateAPIView):
  serializer_class = StackSerializer
  authentication_classes = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]
  queryset = Stack.objects.all()
  


class StackDeleteView(generics.RetrieveDestroyAPIView):
  serializer_class = StackSerializer
  authentication_classes = [authentication.TokenAuthentication]
  permissions_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
  queryset = Stack.objects.all()

  def delete_object(self):
    instance = self.get_object()
    self.perform_destroy(instance)
    return Response({
      "message": "Stack deleted successfully"
    })





# Vistas de ProjectDev

class ProjectDevListView(generics.ListAPIView):
  authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
  queryset = ProjectDev.objects.all()
  serializer_class = ProjectDevSerializer
  permission_classes = [permissions.IsAuthenticated]
  
    
  
  
class ProjectDevCreateView(generics.CreateAPIView):
  serializer_class = ProjectDevSerializer
  permission_classes = [permissions.IsAuthenticated]
  authentication_classes = [authentication.TokenAuthentication]


# class ProjectDevView(generics):
# class ProjectDevView(generics):



# class EmploymentHistoryListView(generics):
  
  
  
# class EmploymentHistoryView(generics):
# class EmploymentHistoryView(generics):
# class EmploymentHistoryView(generics):



# class AcademyListView(generics):
  
  
# class AcademyView(generics):
# class AcademyView(generics):
# class AcademyView(generics):



# class HobbiesExtrasListView(generics):
  
  
# class HobbiesExtrasView(generics):
# class HobbiesExtrasView(generics):
# class HobbiesExtrasView(generics):



# class SkillsListView(generics):
  
  
# class SkillsView(generics):
# class SkillsView(generics):
# class SkillsView(generics):



# class FactsListView(generics):
  
  
# class FactsView(generics):
# class FactsView(generics):
# class FactsView(generics):


