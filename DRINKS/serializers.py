import imp
from attr import field
from itsdangerous import Serializer
from .models import Drink

from rest_framework import serializers

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id' , 'name' , 'des']


