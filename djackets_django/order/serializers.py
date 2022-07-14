from this import d
from rest_framework import serializers

from .models import Order, OrderItem

from product.serializers import serializers as ProductSerializers


class MyOrderItemSerializer(serializers.ModelSerializer):
    product =ProductSerializers()
    class Meta:
        model = OrderItem
        fields = ('price', 'product',  'quantity',)
    
    
class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)
    
    
    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'zipcode',
            'city',
            'state',
            'phone',
            'stripe_token',
            'items',
            'paid_amount',
          
            )

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('price', 'product',  'quantity',)
    
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    
    
    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'zipcode',
            'city',
            'state',
            'phone',
            'stripe_token',
            'items',
          
            )
    
    # overriding the create function
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order