
from rest_framework import serializers
from ..models.computer import Computadora
from ..models.component import Monitor,Altavoz,PlacaBase,Procesador,Teclado,Raton

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