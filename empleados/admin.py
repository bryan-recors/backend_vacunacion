from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from empleados.models import Usuario

#mediante esta funcion agregamos los campos adicionales del useradmin
class MyUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('cedula','fecha_nacimiento','direccion','telefono_movil','estado_vacunacion','tipo_vacuna','fecha_vacunacion','numero_dosis')}),
    )

admin.site.register(Usuario,MyUserAdmin)