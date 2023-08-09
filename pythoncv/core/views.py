from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
  template_name = 'core/index.html'
  # template_name = 'curriculum/forms/form_experiencia.html'

  
  diccionario_contexto = {
    'title': 'PythonCV'
  }
  
  