from rest_framework import serializers
from usuarios.models import Usuarios

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'email', 'username', 'last_name', 'password']


class UserRegisterSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Usuarios
        fields = ['id', 'email', 'username', 'last_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
        
        

    



