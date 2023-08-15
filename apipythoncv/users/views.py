from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, AuthTokenSerializers
from .models import User

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('id')
  serializer_class = UserSerializer
  
class CreateUserView(generics.CreateAPIView):
  serializer_class = UserSerializer
  
class ViewUpdateUserView(generics.RetrieveUpdateAPIView):
  serializer_class = UserSerializer
  authentication_class = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]
  
  def get_object(self):
    return self.request.user
  
class CreateTokenView(ObtainAuthToken):
  serializer_class = AuthTokenSerializers