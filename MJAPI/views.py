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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def list(self, request):
        return Response(self.get_serializer().data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def get_object(self, pk=None):
        obj = get_object_or_404(self.get_queryset(), pk)
        return obj

    def create(self, request):
        return self.create(request)

    def update(self, request, pk):
        obj = self.get_object(pk)
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        obj = self.get_object(pk=pk)
        obj.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class RetailerViewSet(ContactViewSet):
    serializer_class = RetailerSerializer
    queryset = Retailer.objects.all()


class DeliveryPartnerViewSet(ContactViewSet):
    serializer_class = DeliveryPartnerSerializer
    queryset = DeliveryPartner.objects.all()


class CustomerViewSet(ContactViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ProductViewSet(ContactViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(ContactViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
