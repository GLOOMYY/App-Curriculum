from rest_framework import generics, authentication, permissions
from .models import Stack, ProjectDev, EmploymentHistory, Academy, HobbiesExtras, Skills, Facts
from .serializers import StackSerializer, ProjectDevSerializer, EmploymentHistorySerializer, AcademySerializer, HobbiesExtrasSerializer, SkillsSerializer, FactsSerializer

# Create your views here.

class StackListView(generics.ListAPIView):
  queryset = Stack.objects.all()
  serializer_class = StackSerializer
  authentication_class = [authentication.TokenAuthentication]



# class StackView(generics):



# class StackView(generics):



# class StackView(generics):



class ProjectDevListView(generics.ListAPIView):
  authentication_class = [authentication.TokenAuthentication]
  queryset = ProjectDev.objects.all()
  serializer_class = ProjectDevSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  def get_queryset(self):
    user = self.request.user
    queryset = super().get_queryset().filter(user = user)
    return queryset
    
  
  
# class ProjectDevView(generics):
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


