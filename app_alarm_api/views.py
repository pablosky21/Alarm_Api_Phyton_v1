from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AlarmUsuarios
from .models import AlarmComunidad

from .serializers import SerializerUsuario
from .serializers import SerializerComunidad

# Create your views here.


class listaUsuarios(APIView):
    def get(self,request):
        usuario= AlarmUsuarios.objects.all()
        serializers =  SerializerUsuario(usuario,many=True)
        return Response(serializers.data)
        #  def post(self):
        #   pass

    def post(self, request, format=None):
        serializer = SerializerUsuario(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data['alarm_correo'])
            serializer.validated_data['alarm_correo']
            #num_results = AlarmUsuarios.objects.filter(alarm_correo=request.data).count()
            if AlarmUsuarios.objects.filter(alarm_correo=serializer.validated_data['alarm_correo']).exists():
                print("Hi")
            else:

                print("NO")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)



        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class listaComunidades(APIView):
    def get(self, request):
        comunidad = AlarmComunidad.objects.all()
        serializers = SerializerComunidad(comunidad, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = SerializerComunidad(data=request.data)
        if serializer.is_valid():
            print("NO")
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


