#from django.shortcuts import render
# Create your views here.

from django import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics

#models
from .models import Raton,Teclado,Monitor,Computadora,Orden,DetalleOrden, PlacaBase,Altavoz,Procesador,DispositivoSalida,DispositivoEntrada

#serializers
from .serializers import RatonSerializer,TecladoSerializer,MonitorSerializer,ComputadoraSerializer,OrdenSerializer,DetalleOrdenSerializer, PlacaBaseSerializer,AltavozSerializer,ProcesadorSerializer,DispositivoSalidaSerializer,DispositivoEntradaSerializer
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
        #print('----------->',pc.data)
        if pc.data['costo_total'] is not None:
            return pc
        else:
            return Response({"message":"No hay stock"})


class DetalleOrdenViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    '''def create(self,request,*args,**kwargs):
        #print('-------->',request.data.get('computadoras'))
        return Response({"message": request.data.get('computadoras')})

    def create(self,request,*args,**kwargs):
        ordenn = super().create(request,*args,**kwargs)
        print('----------->',ordenn.data)
        return Response({"message":"No hay stock kkkk"})

        if pc.data['costo_total'] is not None:
            return pc
        else:
            return Response({"message":"No hay stock"})'''


class ComponenteTipoView(generics.ListAPIView):#componentetipo/?componente=dispositivoentrada
    serializer_class = DispositivoEntradaSerializer

    def get_queryset(self):

        llave = list(self.request.query_params.keys())[0]# se obtiene el nombre de la variable del parametro
        #print(llave)

        if llave == 'marca':
            marcadisp = self.request.query_params.get(llave)
            entrada = DispositivoEntrada.objects.filter(marca__contains=marcadisp)
            salida = DispositivoSalida.objects.filter(marca__contains=marcadisp)
            return entrada.union(salida)

        elif llave == 'componente':
            # componente trae el valor de llave, llave es el nombre del parametro
            componente = self.request.query_params.get(llave)

            if componente == 'dispositivoentrada':
                dispositivo_entrada = DispositivoEntrada.objects.all()
                return dispositivo_entrada

            elif componente == 'dispositivosalida':
                dispositivo_salida = DispositivoSalida.objects.all()
                return dispositivo_salida

            else:
                return None




        
        

        
        
        



        