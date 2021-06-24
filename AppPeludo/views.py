from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from AppPeludo.models import Mascotas
from AppPeludo.forms import Mascotas, MascotasForm

# Create your views here.

def home(request):
    return render(request,'index.html')

def clima(request):
    return render(request,'clima.html')

def formulario(request):
    return render(request,'formulario.html')


def listamascotas(request):
    mascotas = Mascotas.objects.all()

    return render(request, 'listamascotas.html', {'mascotas': mascotas})

def crearmascotas(request):
    mascota = Mascotas(
        codigo = "M002",
        nombre = "Chris",
        especie = "Perro",
        adoptado = False
    )
    mascota.save()

    return HttpResponse("Registro Creado")

def crearmascotasnav(request, codigo, nombre):
    mascota = Mascotas(
        codigo = codigo,
        nombre = nombre,
        especie = "",
        adoptado = False
    )
    mascota.save()

    return redirect("listamascotas")

def leermascota(request, id):
    mascota = Mascotas.objects.get(id=id)

    return HttpResponse(f"La mascota es: {mascota.codigo},{mascota.nombre}")

def editarmascota(request, id):
    mascota = Mascotas.objects.get(id=id)

    mascota.nombre = "Cachupina"

    mascota.save()

    return HttpResponse(f"Nombre de la mascota actualizado: { mascota.nombre }")

def borrarmascota(request, id):
    mascota = Mascotas.objects.get(id=id)

    mascota.delete()

    return redirect('listamascotas')
#URL


#POR FORMULARIO
def nuevamascota(request):
    return render(request,'nuevamascota.html')

def guardarmascota(request):

    codigo = request.POST['codigo']
    nombre = request.POST['nombre']

    mascota = Mascotas(
        codigo = codigo, 
        nombre = nombre,
        especie = '',
        adoptado = False
    )

    mascota.save()

    return redirect('listamascotas')

#POR FORMULARIO COMPLETO
def formMascota(request):
    datos = {
        'form' : MascotasForm()   
    }
    if request.method=='POST':
        formulario = MascotasForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos Guardados Correctamente"


    return render(request,'nuevamascotaform.html', datos)

def formMascotamod(request, id):
    mascota = Mascotas.objects.get(id=id)
    datos = {
        'form' : MascotasForm(instance=mascota)   
    }
    if request.method=='POST':
        formulario = MascotasForm(data=request.POST,instance=mascota)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos Modificados Correctamente"

    return render(request,'editarmascotaform.html', datos)

def formMascotadel(request, id):
    mascota = Mascotas.objects.get(id=id)
    mascota.delete()


    return redirect('listamascotas')