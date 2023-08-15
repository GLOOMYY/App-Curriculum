from datetime import datetime, date
from users.models import User
from curriculum.models import Habilidades, Tecnologias, Estudios

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

# Procesador de contexto para los skills:
def skill_proccesor(request):
    usuario = request.user

    # Query para traer todos los skills del usuario:
    user_skills = Habilidades.objects.filter(id_user=usuario.id)
    return {
            "skills_user": user_skills
            }


  
# Procesador de contexto para los educación:
def academy_processor(request):
    usuario = request.user
    # Traigo todas las instituciones en donde estudié:
    education_user = Estudios.objects.filter(user=usuario)
    return {
            "education_user": education_user
            }