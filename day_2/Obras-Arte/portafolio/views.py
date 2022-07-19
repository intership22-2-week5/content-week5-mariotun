#from django.shortcuts import render
# Create your views here.

from rest_framework import viewsets

#models
from .models import Tipo,Multimedia,ObrasArte,Author,Author_ObrasArte,Portafolio,Exposicion,User

#serializers
from .serializers import TipoSerializer,MultimediaSerializer,ObrasArteSerializer,AuthorSerializer,Author_ObrasArteSerializer,PortafolioSerializer,ExposicionSerializer,UserSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class MultimediaViewSet(viewsets.ModelViewSet):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer

class ObrasArteViewSet(viewsets.ModelViewSet):
    queryset = ObrasArte.objects.all()
    serializer_class = ObrasArteSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class Author_ObrasArteViewSet(viewsets.ModelViewSet):
    queryset = Author_ObrasArte.objects.all()
    serializer_class = Author_ObrasArteSerializer

class PortafolioViewSet(viewsets.ModelViewSet):
    queryset = Portafolio.objects.all()
    serializer_class = PortafolioSerializer

class ExposicionViewSet(viewsets.ModelViewSet):
    queryset = Exposicion.objects.all()
    serializer_class = ExposicionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer