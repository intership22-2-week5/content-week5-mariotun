from django.db import models

class Componente(models.Model):
    component = (
        ('keyboard','teclado'),
        ('mouse','raton'),
        ('display','monitor'),
        ('speaker','altavoz'),
        ('motherboard','placa base'),
        ('processor','procesador'),
    )
    tipoComponente = models.CharField(max_length=50,choices=component)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.tipoComponente}'


class DispositivoSalida(Componente):
    marca = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.marca}'


class DispositivoEntrada(Componente):
    marca = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.marca}'


class Raton(DispositivoEntrada):
    """Model representing a Raton"""
    cantidad = models.IntegerField()
    costo = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.marca}'


class Teclado(DispositivoEntrada):
    """Model representing a Teclado"""
    cantidad = models.IntegerField()
    costo = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.marca}'


class PlacaBase(DispositivoEntrada):
    cantidad = models.IntegerField()
    costo = models.FloatField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.marca}'

class Procesador(DispositivoEntrada):
    cantidad = models.IntegerField()
    costo = models.FloatField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.marca}'


class Monitor(DispositivoSalida):
    """Model representing a Monitor"""
    cantidad = models.IntegerField()
    costo = models.FloatField()
    #descripcion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.marca}'


class Altavoz(DispositivoSalida):
    cantidad = models.IntegerField()
    costo = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.marca}'


