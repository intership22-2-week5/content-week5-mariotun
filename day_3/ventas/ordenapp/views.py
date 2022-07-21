#from django.shortcuts import render
# Create your views here.

from django import views
from rest_framework import viewsets
from rest_framework.response import Response

#models
from .models import Raton,Teclado,Monitor,Computadora,Orden,PlacaBase,Altavoz,Procesador,DispositivoSalida,DispositivoEntrada

#serializers
from .serializers import RatonSerializer,TecladoSerializer,MonitorSerializer,ComputadoraSerializer,OrdenSerializer,PlacaBaseSerializer,AltavozSerializer,ProcesadorSerializer,DispositivoSalidaSerializer,DispositivoEntradaSerializer
'''
class DispositivoEntradaViewSet(viewsets.ModelViewSet):
    queryset = DispositivoEntrada.objects.all()
    serializer_class = DispositivoEntradaSerializer'''

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


class ComputadoraViewSet(viewsets.ModelViewSet):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer

    def create(self,request,*args,**kwargs):
        pc = super().create(request,*args,**kwargs)
        print('----------->',pc.data)
        if pc.data['costo_total'] is not None:
            return pc
        else:
            return Response({"message":"No hay stock"})


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer