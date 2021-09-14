from django.contrib import admin
from django.urls import path
# para redirigir a las urls de las apps
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('empleados.urls', 'empleados')),
]
