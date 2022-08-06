
from rest_framework import serializers

from ..models.component import PlacaBase,Altavoz,Procesador,DispositivoSalida,DispositivoEntrada,Raton,Teclado,Monitor


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
