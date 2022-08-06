
from rest_framework import generics

from rest_framework import viewsets
from ..models.component import DispositivoEntrada,DispositivoSalida, Raton
from ..models.order import Orden,DetalleOrden 
from ..serializers.order import OrdenSerializer,DetalleOrdenSerializer
from ..serializers.component import DispositivoEntradaSerializer



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


class ComponenteTipoView(generics.ListAPIView):
    serializer_class = DispositivoEntradaSerializer

    def get_queryset(self):

        llave = list(self.request.query_params.keys())[0]# se obtiene el nombre de la variable del parametro
        #print(llave)

        if llave == 'marca': # componentetipo/?marca=hp
            marcadisp = self.request.query_params.get(llave)
            entrada = DispositivoEntrada.objects.filter(marca__contains=marcadisp)
            salida = DispositivoSalida.objects.filter(marca__contains=marcadisp)
            return entrada.union(salida)


        elif llave == 'componente': # componentetipo/?componente=dispositivoentrada
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
        
        elif llave == 'cantidad': # componentetipo/?cantidad=3&tipo=dispositivoentrada
            cantidadd = self.request.query_params['cantidad']
            tipo = self.request.query_params['tipo']
            #print('Cantidad: {} Tipo: {} '.format(cantidadd,tipo))
            

            if tipo == 'dispositivoentrada':
                #print('dentro de dispositivo de entrada')
                dispositivo_entrada = Raton.objects.filter(cantidad__gte=20)
                '''print('TIPO: ',type(dispositivo_entrada))
                for i in dispositivo_entrada:
                    if i.cantidad >= int(cantidadd):
                        resultado += i    
                        #print('dentro de dispositivo de entrada',i.cantidad)'''
                return dispositivo_entrada

            elif tipo == 'dispositivosalida':
                dispositivo_salida = DispositivoSalida.objects.filter(cantidad=cantidadd)
                return dispositivo_salida
            else:
                return None