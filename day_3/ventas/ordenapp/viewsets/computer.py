
from rest_framework.response import Response

from rest_framework import viewsets
from ..models.computer import Computadora
from ..serializers.computer import ComputadoraSerializer

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