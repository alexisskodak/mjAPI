from rest_framework import serializers
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class RetailerSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(required=True)

    class Meta:
        model = Retailer
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        contact_data = validated_data.pop('contact')
        retailer = Retailer.objects.create(**validated_data)
        Contact.objects.create(retailer=retailer, **contact_data)
        return retailer


class DeliveryPartnerSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(required=True)

    class Meta:
        model = DeliveryPartner
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        delivery_partner = DeliveryPartner.objects.create(**validated_data)
        Contact.objects.create(DeliveryPartner=delivery_partner, **contact_data)
        return delivery_partner


class CustomerSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(required=True)
    favoriteShops = RetailerSerializer(many=True)

    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        customer = Customer.objects.create(**validated_data)
        Contact.objects.create(customer=customer, **contact_data)
        return customer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    retailer = RetailerSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer(many=True)
    retailer = RetailerSerializer()
    deliveryPartner = DeliveryPartnerSerializer()

    class Meta:
        model = Order
        fields = '__all__'
