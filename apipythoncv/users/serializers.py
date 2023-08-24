from rest_framework import serializers
from .models import User, Links, ResumeUser
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password


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

    def validate_password(self, value):

        return make_password(value)


    # Borrar borrado logico
    def deleteUser(self, instance, validated_data):
        password = validated_data.pop(None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save()
            
    def delete(self, instance, validated_data):
        pass
    
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
    
    
    
#------------------Los demas modelos------------------------

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'
    
    def createLink(self, validated_data):
        link = Links.objects.create(validated_data)
        return link
    
    def updateLink(self, instance, validated_data):
        link = Links.update(instance, validated_data)
        return link
        
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUser
        fields = '__all__'
    
    def createResume(self, validated_data):
        resume = ResumeUser.objects.create(validated_data)
        return resume
    
    def updateResume(self, instance, validated_data):
        resume = ResumeUser.update(instance, validated_data)
        return resume
        