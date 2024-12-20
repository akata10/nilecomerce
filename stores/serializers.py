from rest_framework import serializers
from . models import *


# CATEGORY SERIALIZER

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
# PRODUCT SERIALIZER
# CART SERIALIZER
# ORDER SERIALIZER
# CHECKOUT SERIALIZER