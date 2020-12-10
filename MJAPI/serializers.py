from rest_framework import serializers
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class RetailerSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Retailer
        fields = '__all__'


class DeliveryPartnerSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = DeliveryPartner
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    favoriteShops = RetailerSerializer()

    class Meta:
        model = Customer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    retailer = RetailerSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()
    retailer = RetailerSerializer()
    deliveryPartner = DeliveryPartnerSerializer()

    class Meta:
        model = Order
        fields = '__all__'
