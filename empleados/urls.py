from django.urls import path
from empleados.views import ListarUsuarios,DetalleUsuario

app_name = 'apps.parroquias'

urlpatterns = [
    path('usuarios/',ListarUsuarios.as_view(),name='usuarios'),
    path('usuarios/<int:id>',DetalleUsuario.as_view(),name='detalle_usuario'),
]
