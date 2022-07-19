from rest_framework import serializers

#models
from .models import Tipo,Multimedia,ObrasArte,Author,Author_ObrasArte,Portafolio,Exposicion,User

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class MultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multimedia
        fields = '__all__'

class ObrasArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObrasArte
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class Author_ObrasArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author_ObrasArte
        fields = '__all__'

class PortafolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portafolio
        fields = '__all__'

class ExposicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposicion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'