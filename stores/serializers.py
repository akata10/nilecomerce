from rest_framework import serializers
from . models import *


# CATEGORY SERIALIZER

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

# PRODUCT SERIALIZER

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'
        
# CART SERIALIZER

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields='__all__'


# ORDER SERIALIZER

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

# CHECKOUT SERIALIZER

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        exclude=['cart','amount','order_status','subtotal','payment_complete','ref']