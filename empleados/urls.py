from django.urls import path
from empleados.views import ListarUsuarios,DetalleUsuario,UserLoginAPIView

app_name = 'apps.parroquias'

urlpatterns = [
    path('usuario/login/',UserLoginAPIView.as_view(),name='login'),
    path('usuarios/',ListarUsuarios.as_view(),name='usuarios'),
    path('usuarios/<int:id>',DetalleUsuario.as_view(),name='detalle_usuario'),
]
