#describews the process of going from a python object to json

from rest_framework import serializers
from .models import Item

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price','is_sold']