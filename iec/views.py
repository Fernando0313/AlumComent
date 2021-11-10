from copy import Error
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from iec.models import UsuarioModel
from iec.serializers import RegistroSerializer

# Create your views here.
class RegistroController(ListCreateAPIView):
    # queryset = UsuarioModel.objects.all()
    serializer_class = RegistroSerializer

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)

        if data.is_valid():
            data.save()
            return Response(data={
                'message': 'Usuario creado exitosamente',
                'content': data.data
            })
        else:
            return Response(data={
                'message': 'Error al crear el usuario',
                'content': data.errors
            })
     
    