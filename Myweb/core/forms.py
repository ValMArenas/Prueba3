from django import forms 
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria, Planta

class RegistroUserForm(UserCreationForm):
    class Meta: 
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class PlantaForm(forms.ModelForm):
    class Meta: 
        model = Planta
        fields = ['idPlanta', 'imagen', 'nombre', 'categoria', 'stock', 'precio']
        labels = {
            'idPlanta': 'Id Planta',
            'imagen': 'Imagen',
            'nombre': 'Nombre',
            'categoria': 'Categoria',
            'stock': 'Stock',
            'precio': 'Precio'
        }
        widgets ={
            'idPlanta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Id Planta',
                    'id': 'idplanta'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre de la planta',
                    'id': 'nombre'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar stock',
                    'id': 'stock'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar precio',
                    'id': 'precio'
                }
            )
        }

