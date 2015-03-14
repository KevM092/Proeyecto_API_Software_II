from rest_framework import serializers
from api.models import Cliente,Evento, Categoria


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('id_cliente','nombre', 'usuario', 'email', 'contrase_a','sexo','administrador')

class postClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre', 'usuario', 'email', 'contrase_a','sexo','administrador')
	   
	   
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id_evento' ,'nombre','fecha','hora','descripcion','email','calificacion','precio', 'estado' , 'imagen' , 'lugar_id_lugar', 
    'categoria_id_categoria', 
    'cliente_id_cliente')

	   
class postEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('nombre','fecha','hora','descripcion','email','calificacion','precio', 'estado' , 'imagen' , 'lugar_id_lugar', 
    'categoria_id_categoria', 
    'cliente_id_cliente')
      
    
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id_categoria','nombre')

class postCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']