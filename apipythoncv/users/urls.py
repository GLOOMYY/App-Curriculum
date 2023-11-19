from django.urls import path, include

from rest_framework import routers

from .views import UserViewSet, CreateUserView, RetreiveUpdateUserView, CreateTokenView, CreateLinkView, RetrieveUpdateDestroyLinkView, CreateResumeView, RetrieveUpdateDestroyResumeView

# from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter() # Objeto para la creación de la ruta

# Implementación de ruta de usuarios:

router.register(r'usuarios', UserViewSet, basename='usuarios')


urlpatterns = [
    # Rutas de usuario
    path('list', UserViewSet.as_view()),
    path('create', CreateUserView.as_view()),
    path('edit', RetreiveUpdateUserView.as_view()),
    path('login', CreateTokenView.as_view()),
    
    # Rutas de Links
    path('links/create', CreateLinkView.as_view()),
    path('resume/create', CreateResumeView.as_view()),
    
    # Rutas de Resumen
    path('links/edit', RetrieveUpdateDestroyLinkView.as_view()),
    path('resume/edit', RetrieveUpdateDestroyResumeView.as_view())
]
