"""FundacionPeludo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppPeludo.views import crearmascotas, crearmascotasnav, home
from AppPeludo.views import clima
from AppPeludo.views import formulario
from AppPeludo.views import listamascotas
from AppPeludo.views import leermascota
from AppPeludo.views import editarmascota
from AppPeludo.views import borrarmascota
from AppPeludo.views import nuevamascota
from AppPeludo.views import guardarmascota
from AppPeludo.views import formMascota
from AppPeludo.views import formMascotamod
from AppPeludo.views import formMascotadel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('home/',home,name='home'),
    path('clima/',clima,name='clima'),
    path('formulario/',formulario,name='formulario'),
    path('listamascotas/',listamascotas,name='listamascotas'),
    path('crearmascotas/',crearmascotas,name='crearmascotas'),
    path('crearmascotasnav/<str:codigo>/<str:nombre>',crearmascotasnav,name='crearmascotasnav'),
    path('leermascota/<int:id>',leermascota,name='leermascota'),
    path('editarmascota/<int:id>',editarmascota,name='editarmascota'),
    path('borrarmascota/<int:id>',borrarmascota,name='borrarmascota'),
    path('nuevamascota/',nuevamascota,name='nuevamascota'),
    path('guardarmascota/',guardarmascota,name='guardarmascota'),
    path('formmascota/',formMascota,name='formmascota'),
    path('formmascotamod/<int:id>',formMascotamod,name='formmascotamod'),
    path('formmascotadel/<int:id>',formMascotadel,name='formmascotadel'),
]

