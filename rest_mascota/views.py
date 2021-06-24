from datetime import date
from django.http import request
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from AppPeludo.models import Mascotas
from .serializers import MascotasSerializers

@csrf_exempt
@api_view(['GET','POST'])
def lista_mascotas(request):
    if request.method == 'GET':
        mascota = Mascotas.object.all()
        serializers = MascotasSerializers(mascota, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = MascotasSerializers(data = data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


