from django.db import models

from .computer import Computadora

class Orden(models.Model):
    """Model representing an Orden"""
    #computadoras = models.ManyToManyField(Computadora)
    name = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    #total_costo_orden = models.FloatField(null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    '''def save(self,*args,**kwargs):
        #print('-------->', self.request.data)
        result = self.computadoras.values_list('id',flat=True)
        print('rrrrr ',result)
        #super(Orden,self).save(*args,**kwargs)
        #orden = Orden.objects.filter(id=self.id)
        #print(orden)

    def decrementar_computadoras(self,lista_computadoras):
        print('lista ->',lista_computadoras)
        

        return True'''
        
        

class DetalleOrden(models.Model):
    """Model representing an DetalleOrden"""
    orden = models.ForeignKey(Orden,on_delete=models.CASCADE)
    computadoras = models.ForeignKey(Computadora,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    costo_total =  models.FloatField(null=True,blank=True)

    def __str__(self):
        return f'{self.costo_total}'

    def decrementar_cantidad(self):
        pass

    def save(self,*args,**kwargs):
        self.costo_total = self.cantidad * (self.computadoras.costo_total)
        super(DetalleOrden,self).save(*args,**kwargs)

'''
self.costo_total = self.monitor.costo + self.altavoz.costo + self.placaBase.costo + self.procesador.costo + self.raton.costo+ self.teclado.costo

        Monitor.objects.filter(id=self.monitor.id).update(cantidad = models.F('cantidad')-1)
        Altavoz.objects.filter(id=self.altavoz.id).update(cantidad = models.F('cantidad')-1)
        PlacaBase.objects.filter(id=self.placaBase.id).update(cantidad = models.F('cantidad')-1)
        Procesador.objects.filter(id=self.procesador.id).update(cantidad = models.F('cantidad')-1)
        Raton.objects.filter(id=self.raton.id).update(cantidad = models.F('cantidad')-1)
        Teclado.objects.filter(id=self.teclado.id).update(cantidad = models.F('cantidad')-1)

        super(Computadora,self).save(*args,**kwargs)

        return self.costo_total
'''