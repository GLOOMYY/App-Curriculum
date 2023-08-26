from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, AuthTokenSerializers, LinkSerializer, ResumeSerializer
from .models import User, Links, ResumeUser

# Create your views here.

# --------------- Vistas de Users ---------------

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('id')
  serializer_class = UserSerializer
  
class CreateUserView(generics.CreateAPIView):
  serializer_class = UserSerializer
  
class RetreiveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # Obtenemos el usuario logueado
    def get_object(self):
        return self.request.user
      
      
class CreateTokenView(ObtainAuthToken):
  serializer_class = AuthTokenSerializers
  
class DeleteUserView(generics.RetrieveUpdateAPIView):
  pass

# --------------- Vistas de Link ---------------

class CreateLinkView(generics.CreateAPIView):
  serializer_class = LinkSerializer
  authentication_class = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]
  
class GetLinkView(generics.ListAPIView):
  serializer_class = LinkSerializer
  authentication_class = [authentication.TokenAuthentication]
  
class RetrieveUpdateDestroyLinkView(generics.RetrieveUpdateDestroyAPIView):
  # Arreglar el edit usando foreing key
  serializer_class = LinkSerializer
  authentication_class = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]
  
# --------------- Vistas de Resumen ---------------
  
class CreateResumeView(generics.CreateAPIView):
  serializer_class = ResumeSerializer
  authentication_class = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]
  
class GetResumeView(generics.ListAPIView):
  serializer_class = ResumeSerializer
  authentication_class = [authentication.TokenAuthentication]
  
class RetrieveUpdateDestroyResumeView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ResumeSerializer
  authentication_class = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]