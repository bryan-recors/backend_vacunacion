from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer,UserLoginSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

class UserLoginAPIView(APIView):
    def post(self, request, *args, **Kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
          'user': UsuarioSerializer(user).data,
          'access_token': token
        }
        return Response(data,status=status.HTTP_201_CREATED)

class ListarUsuarios(APIView):
    # metodo http
    def get(self, request):
        # consulto los registros de parroquias y lo guardo en la variable parroquias
        usuarios = Usuario.objects.filter(is_superuser=False)
        usuario_json = UsuarioSerializer(usuarios, many=True)
        # como lo que vamos a enviar como respuesta esta en formato json necesito usar la clase response
        return Response(usuario_json.data)

    # para crear un registro
    def post(self, request):
        usuario_json = UsuarioSerializer(data=request.data)  # unmarshal
        if usuario_json.is_valid():
            # si fue corecto lo persistimos
            usuario_json.save()
            # si se creo correctamente lo retornamos con la clase Response
            return Response(usuario_json.data, status=201)
        # si no se creo correctamente
        return Response(usuario_json.errors, status=400)

class DetalleUsuario(APIView):
    # obtener el objeto de acuerdo al id que recibe
    def get_object(self, id):
        try:
            return Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            usuario = get_object_or_404(Usuario, pk=id)

    # mostrar una parroquia de acuerdo a su id
    def get(self,request,id):
        usuario = self.get_object(id)
        usuario_json = UsuarioSerializer(usuario) # solo es un objeto no se usa many
        # como lo que vamos a enviar como respuesta esta en formato json necesito usar la clase response
        return Response(usuario_json.data)

    #actualizar registro de una parroquia
    def put(self,request,id):
        usuario = self.get_object(id)
        usuario_json = UsuarioSerializer(usuario, data=request.data)
        if usuario_json.is_valid():
            usuario_json.save() #guardar el objeto ya serializado
            return Response(usuario_json.data) # retorno los datos
        return Response(usuario_json.errors, status=400) #si no se pudo crear

    # eliminar proveedor
    def delete(self, request, id):
        usuario = self.get_object(id)
        usuario.delete()
        return Response(status=204)  # como ya se elimino no encontro ningun contenido