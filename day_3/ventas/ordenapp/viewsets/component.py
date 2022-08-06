
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics

from ..models.component import PlacaBase,Altavoz,Procesador,DispositivoSalida,DispositivoEntrada,Raton,Teclado,Monitor

from ..serializers.component import PlacaBaseSerializer,AltavozSerializer,ProcesadorSerializer,DispositivoSalidaSerializer,DispositivoEntradaSerializer,RatonSerializer,TecladoSerializer,MonitorSerializer

class PlacaBaseViewSet(viewsets.ModelViewSet):
    queryset = PlacaBase.objects.all()
    serializer_class = PlacaBaseSerializer


class AltavozViewSet(viewsets.ModelViewSet):
    queryset = Altavoz.objects.all()
    serializer_class = AltavozSerializer


class ProcesadorViewSet(viewsets.ModelViewSet):
    queryset = Procesador.objects.all()
    serializer_class = ProcesadorSerializer


class DispositivoSalidaViewSet(viewsets.ModelViewSet):
    queryset = DispositivoSalida.objects.all()
    serializer_class = DispositivoSalidaSerializer


class DispositivoEntradaViewSet(viewsets.ModelViewSet):
    queryset = DispositivoEntrada.objects.all()
    serializer_class = DispositivoEntradaSerializer




class RatonViewSet(viewsets.ModelViewSet):
    queryset = Raton.objects.all()
    serializer_class = RatonSerializer


class TecladoViewSet(viewsets.ModelViewSet):
    queryset = Teclado.objects.all()
    serializer_class = TecladoSerializer


class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
