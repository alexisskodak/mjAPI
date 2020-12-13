from rest_framework import viewsets
from .models import *
from .serializers import *


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class RetailerViewSet(viewsets.ModelViewSet):
    serializer_class = RetailerSerializer
    queryset = Retailer.objects.all()

    def get_retailer_by_city(self, request):
        city = request.GET.get('city')
        return self.queryset.filter(city=city)


class DeliveryPartnerViewSet(viewsets.ModelViewSet):
    serializer_class = DeliveryPartnerSerializer
    queryset = DeliveryPartner.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(viewsets.ViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
