from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import tablaproducto, tablacompra, tablausuario
from .forms import CustomUserCreationForm,ProductoForm,CompraForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User 

# Create your views here.

def index(request): 
    return render(request, 'index.html') 
def registro(request):
    data= {
        'form':CustomUserCreationForm()
    }    
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="index")
        data['form'] = formulario
    return render(request, 'registration/registro.html',data)
@login_required
def log(request):
    return render(request, 'registration/login.html')
@login_required
def productos(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto enviado exitosamente"
        else:
            data["form"] = formulario
    return render(request, 'productos.html',data)
@login_required
def crudproductos(request):
    productos = tablaproducto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'crudproductos.html',data)
@login_required
def modproductos(request,id):
    productos = get_object_or_404(tablaproducto, id=id)
    data = {
        'form': ProductoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=productos,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se ha modificado correctamente"
            return redirect(to="crudproductos")
        data['form'] = formulario
    return render(request, 'modproductos.html',data)
@login_required
def deleteproductos(request,id):
    compras = get_object_or_404(tablaproducto, id=id)
    compras.delete()
    return redirect(to="crudproductos")
@login_required
def compras(request):
    data = {
        'form': CompraForm()
    }
    if request.method == 'POST':
        formulario = CompraForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Compra hecha exitosamente"
        else:
            data["form"] = formulario
    return render(request, 'comprass.html',data)
@login_required
def crudcompras(request):
    compras = tablacompra.objects.all()
    data = {
        'compras': compras
    }
    return render(request, 'crudcomprass.html',data)
@login_required
def modcompras(request,id):
    compras = get_object_or_404(tablacompra, id=id)
    data = {
        'form': CompraForm(instance=compras)
    }

    if request.method == 'POST':
        formulario = CompraForm(data=request.POST,instance=compras,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se ha modificado correctamente"
            return redirect(to="crudcompras")
        data['form'] = formulario
    return render(request, 'modcomprass.html',data)
@login_required
def deletecompras(request,id):
    compras = get_object_or_404(tablacompra, id=id)
    compras.delete()
    return redirect(to="crudcompras")


