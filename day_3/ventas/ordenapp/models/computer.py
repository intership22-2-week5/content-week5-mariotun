from django.db import models

from .component import Monitor,Altavoz,PlacaBase,Procesador,Raton,Teclado

class Computadora(models.Model):
    """Model representing a Computadora"""
    nombre = models.CharField(max_length=100)
    monitor = models.ForeignKey(Monitor,on_delete=models.CASCADE)
    altavoz = models.ForeignKey(Altavoz,on_delete=models.CASCADE)
    placaBase = models.ForeignKey(PlacaBase,on_delete=models.CASCADE)
    procesador = models.ForeignKey(Procesador,on_delete=models.CASCADE)
    raton = models.ForeignKey(Raton,on_delete=models.CASCADE)
    teclado = models.ForeignKey(Teclado,on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    costo_total = models.FloatField(null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre}'
    

    def decrementar_cantidad(self):
        monitor = Monitor.objects.filter(id=self.monitor.id)
        altavoz = Altavoz.objects.filter(id=self.altavoz.id)
        placabase = PlacaBase.objects.filter(id=self.placaBase.id)
        procesador = Procesador.objects.filter(id=self.procesador.id)
        raton = Raton.objects.filter(id=self.raton.id)
        teclado = Teclado.objects.filter(id=self.teclado.id)

        if monitor[0].cantidad >= self.cantidad and altavoz[0].cantidad >= self.cantidad and placabase[0].cantidad >= self.cantidad and procesador[0].cantidad >= self.cantidad and raton[0].cantidad >= self.cantidad and teclado[0].cantidad >= self.cantidad :

            '''Decremento de existencia'''
            #Monitor.objects.filter(id=self.monitor.id).update(cantidad=models.F('cantidad')- self.cantidad)
            monitor.update(cantidad=models.F('cantidad')- self.cantidad)
            altavoz.update(cantidad=models.F('cantidad')- self.cantidad)
            placabase.update(cantidad=models.F('cantidad')- self.cantidad)
            procesador.update(cantidad=models.F('cantidad')- self.cantidad)
            raton.update(cantidad=models.F('cantidad')- self.cantidad)
            teclado.update(cantidad=models.F('cantidad')- self.cantidad)

            total = self.monitor.costo + self.altavoz.costo + self.placaBase.costo + self.procesador.costo + self.raton.costo+ self.teclado.costo

            return total
        else:
            return 0       

    def save(self,*args,**kwargs):
        resultado = self.decrementar_cantidad()
        #print('>>>>>RRRRR>>>>>>',resultado)
        if resultado>0:
            self.costo_total = resultado
            super(Computadora,self).save(*args,**kwargs)
        else:
            return False

    '''def save(self,*args,**kwargs):
        """Funcion para reducir en el stock de monitores"""
        Monitor.objects.filter(id=self.monitor.id).update(contadorMonitores = models.F('contadorMonitores')-1)
        Raton.objects.filter(id=self.raton.id).update(contadorRatones = models.F('contadorRatones')-1)
        Teclado.objects.filter(id=self.teclado.id).update(contadorTeclados = models.F('contadorTeclados')-1)
        super(Computadora,self).save(*args,**kwargs)'''
