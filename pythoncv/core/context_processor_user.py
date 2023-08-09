from datetime import datetime, date
from users.models import User
from curriculum.models import Habilidades, Tecnologias, Estudios
from django.contrib.auth.decorators import login_required

#implementar todo por este context proccesor

# Procesador de contexto para calcular la edad
def age_proccesor(request):
  if request.user.is_authenticated:
    usuario = request.user
    fecha_nacimiento = usuario.birthday

    try:
      if datetime.now().month <= fecha_nacimiento.month and datetime.now().day >= fecha_nacimiento.day:
        edad = (datetime.now().year-1) - fecha_nacimiento.year
      else:
        edad = datetime.now() - fecha_nacimiento.year
    except:
      edad= 'No es posible calcular la edad' 
    
    return {
                'edad':edad,
                'usuario':usuario
            }
  else:
    return { 'mensaje':"Usuario no autenticado" }

@login_required()
def skill_proccesor(request):
  user_skills = Habilidades.objects.filter(id_user=request.user.id)
  print(user_skills)
  
    
  
  return {
            'skills':user_skills,
          }
  
@login_required()
def academy_proccesor(request):
  #Todas las instituciones donde estudio
  education_user = Estudios.objects.filter(user=request.user).order_by('finish_date')
  return {
    
  }