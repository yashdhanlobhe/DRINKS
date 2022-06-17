from ast import Return
import imp
from os import stat
import django
from django.http import JsonResponse
from httplib2 import Response
from itsdangerous import Serializer
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from DRINKS import serializers



@api_view(['GET' , 'POST'])
def drink_list(req):

    if req.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks , many = True)
        return JsonResponse({"drinks" : serializer.data })
    if req.method == 'POST':
        serializer = DrinkSerializer(data = req.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        

@api_view(['GET' , 'PUT' , 'DELETE'])
def drink_details(req , id):
    
    try:
        drink = Drink.objects.get(pk = id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'GET':
        ser = DrinkSerializer(drink)
        return Response(ser.data) 
    elif req.method == 'PUT':
        ser = DrinkSerializer(data = req.data)
        if ser.is_valid():
            ser.save()
            return Response(serializers.data)

    elif req.method == 'DELETE':
        drink.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    