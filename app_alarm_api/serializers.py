from rest_framework import serializers
from .models import AlarmUsuarios
from .models import AlarmComunidad

class SerializerUsuario(serializers.ModelSerializer):

    class Meta:
        model = AlarmUsuarios
        # fields = 'alarm_nombre,alarm_apelldio'
        fields = '__all__'


class SerializerComunidad(serializers.ModelSerializer):
    class Meta:
        model = AlarmComunidad
        # fields = 'alarm_nombre,alarm_apelldio'
        fields = '__all__'