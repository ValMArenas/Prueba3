from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Categoria, Planta
from .forms import PlantaForm, RegistroUserForm, User
from core.compras import Carrito


# Create your views here.
def index(request):
    return render (request, 'index.html')

@login_required
def productos(request):
    plantas = Planta.objects.all()             
    return render(request, 'productos.html', {'plantas':plantas})

def crear(request):
    if request.method=='POST':
        plantaform = PlantaForm(request.POST, request.FILES)
        if plantaform.is_valid():
            plantaform.save()         
            return redirect ('productos')
    else:
        plantaform=PlantaForm()
    return render(request, 'crear.html',{'plantaform':plantaform})

def detalle_planta(request, id):
    planta = get_object_or_404(Planta, idPlanta=id) 
    return render (request, 'detallePlanta.html', {'planta': Planta})

def modificar(request, id):
    planta = Planta.objects.get(idPlanta=id)
    datos={
        'forModificar': PlantaForm(instance=planta),
        'planta':  Planta
    }
    if request.method=='POST':
        formulario= PlantaForm(request.POST, request.FILES, instance=planta)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos')
    return render(request, 'modificar.html', datos)


def eliminar(request, id):
    planta = get_object_or_404(Planta, idPlanta=id)
    if request.method=='POST':
        if 'elimina' in request.POST:       
            planta.delete()
            return redirect ('productos')
        else:
            return redirect ('detalle', idPlanta=id)
    return render (request, 'eliminar.html', {'planta': Planta})
        
def cerrar(request):
    logout(request)
    return redirect('index')

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=='POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('index')
        data["form"]=formulario
    return render(request, 'registration/registrar.html',data)

def nosotras(request):
    return render (request, 'nosotras.html')

def contacto(request):
    return render (request, 'contacto.html')

def sucursales(request):
    return render (request, 'sucursales.html')

def perfil(request):
    return render (request, 'perfil.html')

def carrito(request):
    return render (request, 'carrito.html')

def detalle_user(request, id):
    User = get_object_or_404(User, username=id) 
    return render (request, 'perfil.html', {'user':User})

def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    planta = Planta.objects.get(idPlanta=id)
    carrito_compra.agregar(planta=planta)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    planta = Planta.objects.get(idPlanta=id)
    carrito_compra.eliminar(planta=planta)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    planta = Planta.objects.get(idPlanta=id)
    carrito_compra.restar(planta=planta)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    

def tienda(request):
    plantas = Planta.objects.all()
    datos={
        'plantas':plantas
    }
    return render(request, 'tienda.html', datos)


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Planta.objects.get(idPlanta = value['planta_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)
