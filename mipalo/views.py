from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from .models import tablaproducto, tablacompra
from .forms import CustomUserCreationForm,ProductoForm,CompraForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User 
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

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
@permission_required('mipalo.add_tablaproducto')
def productos(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto enviado exitosamente")
            #data["mensaje"] = "Producto enviado exitosamente"
        else:
            data["form"] = formulario
    return render(request, 'productos.html',data)
@login_required
@permission_required('mipalo.view_tablaproducto')
def crudproductos(request):
    productos = tablaproducto.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productos,5)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'crudproductos.html',data)
@login_required
@permission_required('mipalo.change_tablaproducto')
def modproductos(request,id):
    productos = get_object_or_404(tablaproducto, id=id)
    data = {
        'form': ProductoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=productos,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            #data["mensaje"] = "Se ha modificado correctamente"
            return redirect(to="crudproductos")
        data['form'] = formulario
    return render(request, 'modproductos.html',data)
@login_required
@permission_required('mipalo.delete_tablaproducto')
def deleteproductos(request,id):
    compras = get_object_or_404(tablaproducto, id=id)
    compras.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to="crudproductos")
@login_required
@permission_required('mipalo.add_tablacompra')
def compras(request):
    data = {
        'form': CompraForm()
    }
    if request.method == 'POST':
        formulario = CompraForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Compra hecha exitosamente")
            #data["mensaje"] = "Compra hecha exitosamente"
        else:
            data["form"] = formulario
    return render(request, 'comprass.html',data)
@login_required
@permission_required('mipalo.view_tablacompra')
def crudcompras(request):
    compras = tablacompra.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(compras,5)
        compras = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity': compras,
        'paginator': paginator
    }
    return render(request, 'crudcomprass.html',data)
@login_required
@permission_required('mipalo.change_tablacompra')
def modcompras(request,id):
    compras = get_object_or_404(tablacompra, id=id)
    data = {
        'form': CompraForm(instance=compras)
    }

    if request.method == 'POST':
        formulario = CompraForm(data=request.POST,instance=compras,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            #data["mensaje"] = "Se ha modificado correctamente"
            messages.success(request,"Modificado Correctamente")
            return redirect(to="crudcompras")
        data['form'] = formulario
    return render(request, 'modcomprass.html',data)
@login_required
@permission_required('mipalo.delete_tablacompra')
def deletecompras(request,id):
    compras = get_object_or_404(tablacompra, id=id)
    compras.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to="crudcompras")


