from django.db import models
# Create your models here.

class DispositivoEntrada(models.Model):
    """Model representing a DispositivoEntrada"""
    tipoEntrada = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.tipoEntrada} - {self.marca}'

    class Meta:
        abstract = True


class Raton(DispositivoEntrada):
    """Model representing a Raton"""
    contadorRatones = models.IntegerField()

    def __str__(self):
        return f'{self.marca}'


class Teclado(DispositivoEntrada):
    """Model representing a Teclado"""
    contadorTeclados = models.IntegerField()

    def __str__(self):
        return f'{self.marca}'


class Monitor(models.Model):
    """Model representing a Monitor"""
    marca = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
    contadorMonitores = models.IntegerField()

    def __str__(self):
        return f'{self.marca}'


class Computadora(models.Model):
    """Model representing a Computadora"""
    nombre = models.CharField(max_length=100)
    monitor = models.ForeignKey(Monitor,on_delete=models.CASCADE)
    teclado = models.ForeignKey(Teclado,on_delete=models.CASCADE)
    raton = models.ForeignKey(Raton,on_delete=models.CASCADE)
    contadorComputadoras = models.IntegerField()

    def save(self,*args,**kwargs):
        """Funcion para reducir en el stock de monitores"""
        Monitor.objects.filter(id=self.monitor.id).update(contadorMonitores = models.F('contadorMonitores')-1)
        Raton.objects.filter(id=self.raton.id).update(contadorRatones = models.F('contadorRatones')-1)
        Teclado.objects.filter(id=self.teclado.id).update(contadorTeclados = models.F('contadorTeclados')-1)
        super(Computadora,self).save(*args,**kwargs)


    def __str__(self):
        return f'{self.nombre} - {self.contadorComputadoras}'

class Orden(models.Model):
    """Model representing an Orden"""
    computadoras = models.ManyToManyField(Computadora)
    contadorOrdenes = models.IntegerField()

    def __str__(self):
        return f'{self.computadoras}'