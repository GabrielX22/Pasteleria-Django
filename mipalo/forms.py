from django import forms
from django.forms import ModelForm, ValidationError
from .models import tablaproducto
from .models import tablacompra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import maximotamano


class ProductoForm(forms.ModelForm):

    producto = forms.CharField(min_length=3,max_length=50)
    tipoproducto = forms.CharField(min_length=3,max_length=100)
    marcaproducto = forms.CharField(min_length=1,max_length=100)
    productoimagen = forms.ImageField(required=False, validators=[maximotamano(max_file_size=10)])
    stockproducto = forms.IntegerField(min_value=1,max_value=1000)
    precioproducto = forms.DecimalField(min_value=0.10,max_value=999.99)

    def clean_producto(self):
        producto = self.cleaned_data["producto"]
        existente = tablaproducto.objects.filter(producto__iexact=producto).exists()

        if existente:
            raise ValidationError("Este nombre ya existe")

        return producto

    class Meta:
        model = tablaproducto
        fields = '__all__'

        widgets = {
            "fechaproducto": forms.SelectDateWidget()
        }
class CompraForm(forms.ModelForm):

    cliente = forms.CharField(min_length=2,max_length=15)
    nombrecompra = forms.CharField(min_length=2,max_length=100)
    compraimagen = forms.ImageField(required=False, validators=[maximotamano(max_file_size=10)])
    cantidadcompra = forms.IntegerField(min_value=1,max_value=1000)
    preciocompra = forms.DecimalField(min_value=0.10,max_value=999.99)
    preciototal = forms.DecimalField(min_value=0.10,max_value=999.99)

    class Meta:
        model = tablacompra
        fields = '__all__'

        widgets = {
            "fechacompras": forms.SelectDateWidget()
        }
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','password1','password2']