from django.contrib import admin
from mipalo.models import tablausuario,tablacompra,tablaproducto
from .forms import ProductoForm,CompraForm
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm

class CompraAdmin(admin.ModelAdmin):
    form = CompraForm

admin.site.register(tablausuario) 
admin.site.register(tablacompra)
admin.site.register(tablaproducto)