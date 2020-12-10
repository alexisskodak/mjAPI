from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import *
from .serializers import *


class ContactViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    """
    Read only ViewSet since Contacts should be created by children Objects
    such as Retailer, Delivery Partners and Customers
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def list(self, request):
        return Response(self.get_serializer().data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        contact = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(contact)
        return Response(serializer.data)


class RetailerViewSet(ContactViewSet):
    """
    Basic CRUD ViewSet from which the other ones inherit
    TODO: Filter
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RetailerSerializer
    queryset = Retailer.objects.all()

    def get_object(self, pk=None):
        retailer = get_object_or_404(self.get_queryset(), pk)
        return retailer

    def create(self, request):
        return self.create(request)

    def update(self, request, pk):
        retailer = self.get_object(pk)
        serializer = self.get_serializer(retailer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        retailer = self.get_object(pk=pk)
        retailer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class DeliveryPartnerViewSet(RetailerViewSet):
    serializer_class = DeliveryPartnerSerializer
    queryset = DeliveryPartner.objects.all()


class CustomerViewSet(RetailerViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ProductViewSet(RetailerViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(RetailerViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
