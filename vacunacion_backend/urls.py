from django.contrib import admin
from django.urls import path
# para redirigir a las urls de las apps
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('empleados.urls', 'empleados')),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
