from rest_framework import serializers
from .models import Usuario
#django para autenticar
from django.contrib.auth import authenticate
#Token
from rest_framework.authtoken.models import Token

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        # modelo a serializar
        model = Usuario
        # tupla con los elelmentos a serializar
        fields = ('id','cedula','nombres','apellidos', 'email', 'username','fecha_nacimiento', 'direccion', 'telefono_movil',
                  'estado_vacunacion', 'tipo_vacuna','fecha_vacunacion', 'numero_dosis')

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        #validar credenciales
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credenciales invalidas')
        self.context['user'] = user
        return data
    #manejar el Token
    def create(self, data):
       #generar un new token
       token, created = Token.objects.get_or_create(user=self.context['user'])
       return self.context['user'],token.key