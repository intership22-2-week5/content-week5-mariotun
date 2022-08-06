
from rest_framework import serializers
from ..models.order import Orden,DetalleOrden
from ..models.computer import Computadora

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