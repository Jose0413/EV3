from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Mascotas

class MascotasForm(ModelForm):

    class Meta:
        model = Mascotas
        fields = ['codigo','nombre','especie','adoptado']