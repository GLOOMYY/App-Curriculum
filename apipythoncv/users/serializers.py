from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate, get_user_model



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        
    def createUser(self, validated_data):
        return get_user_model.objects.create_user(**validated_data)
    
    def updateUser(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save()
        
        return user
    
class AuthTokenSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )
        
        if not user:
            raise serializers.ValidationError('El usuario no se pudo autenticar', code='authorization')
        
        attrs['user'] = user
        
        return attrs