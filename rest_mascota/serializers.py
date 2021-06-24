from django.db.models import fields
from rest_framework import serializers
from AppPeludo.models import Mascotas

class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = ['codigo','nombre','especie','adoptado']