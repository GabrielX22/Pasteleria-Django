from django import forms
from django.forms import ModelForm
from .models import tablaproducto
from .models import tablacompra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    class Meta:
        model = tablaproducto
        fields = '__all__'

        widgets = {
            "fechaproducto": forms.SelectDateWidget()
        }
class CompraForm(forms.ModelForm):
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