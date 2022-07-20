from rest_framework import serializers
import json
#models
from .models import Raton,Teclado,Monitor,Computadora,Orden
'''
class DispositivoEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispositivoEntrada
        fields = '__all__' '''


class RatonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raton
        fields = '__all__'


class TecladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teclado
        fields = '__all__'


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'


class ComputadoraSerializer(serializers.ModelSerializer):
    raton = serializers.PrimaryKeyRelatedField(queryset=Raton.objects.all())
    teclado = serializers.PrimaryKeyRelatedField(queryset=Teclado.objects.all())
    monitor = serializers.PrimaryKeyRelatedField(queryset=Monitor.objects.all())

    class Meta:
        model = Computadora
        fields = '__all__'

    def to_representation(self,instance):
        return{
            'nombre': instance.nombre,
            'monitor':instance.monitor.marca,
            'teclado':instance.teclado.marca,
            'raton':instance.raton.marca,
        }


class OrdenSerializer(serializers.ModelSerializer):
   # compu = serializers.PrimaryKeyRelatedField(queryset=Computadora.objects.all())

    class Meta:
        model = Orden
        fields = '__all__'
    '''
    def to_representation(self,instance):
        return{
            #'computadoras':json.dumps(Orden.computadoras)
            'computadoras':{instance.computadoras}
        }'''