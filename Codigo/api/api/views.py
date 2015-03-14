from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import *
from serializers import *

####inicio
@api_view(['GET', 'POST'])
def Cliente_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Cliente.objects.all()
        serializer = ClienteSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =postClienteSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Cliente_detail(request, pk):

    """
    Get, udpate, or delete a specific task
    """
    try:
        task = Cliente.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClienteSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
##Finn


####inicio Evento
@api_view(['GET', 'POST'])
def Evento_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Evento.objects.all()
        serializer = EventoSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =postEventoSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Evento_detail(request, pk):

    """
    Get, udpate, or delete a specific task
    """
    try:
        task = Evento.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventoSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventoSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
##Finn