
from http.cookies import Morsel
from statistics import mode
from django.db import models

# Create your models here.

class Tipo(models.Model):
    """Model representing an Tipo"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name} - {self.description}'

class Multimedia(models.Model):
    """Model representing an Multimedia"""
    name = models.CharField(max_length=100)
    uri = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name} - {self.description}'

class ObrasArte(models.Model):
    """Model representing a ObrasArte"""
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    multimedia = models.ForeignKey(Multimedia,on_delete=models.CASCADE)
 
    def __str__(self):
        return f'{self.name} - {self.price}'

class Author(models.Model):
    """ Model representing an author """
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.description}'

class Author_ObrasArte(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    obrasarte = models.ForeignKey(ObrasArte,on_delete=models.CASCADE)

def __str__(self):
        return f'{self.author} - {self.obrasarte}'

class Portafolio(models.Model):
    """ Model representing an portafolio """
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    obrasarte =models.ForeignKey(ObrasArte,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.description}'

class Exposicion(models.Model):
    """Model representing an exposition"""
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    place = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    Portafolio = models.ForeignKey(Portafolio,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.place}'

class User(models.Model):
    """Model representing an user"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    exposicion =models.ForeignKey(Exposicion,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} - {self.email}'


