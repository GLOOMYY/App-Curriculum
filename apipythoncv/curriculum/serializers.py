from rest_framework import serializers
from .models import Stack, ProjectDev, EmploymentHistory, Academy, HobbiesExtras, Skills, Facts


class StackSerializer(serializers.ModelSerializer):
  class Meta:
    model = Stack
    fields = '__all__'
    

class ProjectDevSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectDev
    fields = '__all__'


class EmploymentHistorySerializer(serializers.ModelSerializer):
  class Meta:
    model = EmploymentHistory
    fields = '__all__'


class AcademySerializer(serializers.ModelSerializer):
  class Meta:
    model = Academy
    fields = '__all__'


class HobbiesExtrasSerializer(serializers.ModelSerializer):
  class Meta:
    model = HobbiesExtras
    fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skills
    fields = '__all__'


class FactsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Facts
    fields = '__all__'
    