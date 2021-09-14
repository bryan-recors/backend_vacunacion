from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        # modelo a serializar
        model = Usuario
        # tupla con los elelmentos a serializar
        fields = ('id','cedula','nombres','apellidos', 'email', 'username','fecha_nacimiento', 'direccion', 'telefono_movil',
                  'estado_vacunacion', 'tipo_vacuna','fecha_vacunacion', 'numero_dosis')