from rest_framework import serializers
import json
#models
from .models import Raton,Teclado,Monitor,Computadora,Orden,DetalleOrden,PlacaBase,Altavoz,Procesador,DispositivoSalida,DispositivoEntrada
'''
class DispositivoEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispositivoEntrada
        fields = '__all__' '''

class PlacaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaBase
        fields = '__all__'


class AltavozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Altavoz
        fields = '__all__'


class ProcesadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procesador
        fields = '__all__'

class DispositivoSalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispositivoSalida
        fields = '__all__'


class DispositivoEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispositivoEntrada
        fields = '__all__'




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
    '''
    raton = serializers.PrimaryKeyRelatedField(queryset=Raton.objects.all())
    teclado = serializers.PrimaryKeyRelatedField(queryset=Teclado.objects.all())
    monitor = serializers.PrimaryKeyRelatedField(queryset=Monitor.objects.all())
    placabase = serializers.PrimaryKeyRelatedField(queryset=PlacaBase.objects.all())
    procesador = serializers.PrimaryKeyRelatedField(queryset=Procesador.objects.all())
    altavoz = serializers.PrimaryKeyRelatedField(queryset=Altavoz.objects.all())'''

    class Meta:
        model = Computadora
        fields = '__all__'

    def to_representation(self,instance):
        return{
            'nombre': instance.nombre,
            'monitor':{
                #'marca':instance.monitor.marca,
                'marca':instance.monitor.marca,
            },
            'altavoz': instance.altavoz.marca,
            'placabase':instance.placaBase.marca,
            'procesador':instance.procesador.marca,
            'teclado':instance.teclado.marca,
            'raton':instance.raton.marca,
            'costo_total': instance.costo_total
        }


class OrdenSerializer(serializers.ModelSerializer):
    #compu = serializers.PrimaryKeyRelatedField(queryset=Computadora.objects.all())
    
    class Meta:
        model = Orden
        fields = '__all__'
    '''
    def to_representation(self,instance):
        # print('mmmmmmmmmmm', instance.computadoras.get())
        return{
            #'computadoras':json.dumps(Orden.computadoras)
            'computadoras':instance.coputadoras
        }'''

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = '__all__'

    def to_representation(self,instance):
        return{
            'id':instance.id,
            'orden':instance.orden.name,
            'cantidad_computadoras': instance.cantidad,
            'computadora':{
                'nombre':instance.computadoras.nombre,
                'costo_total':instance.computadoras.costo_total
            },
            'costo_total_orden': instance.costo_total
        }