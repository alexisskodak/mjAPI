from django.urls import path
from .views import *

urlpatterns = [
    path('contacts/', ContactViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        })),
    path('contacts/<int:pk>/', ContactViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })),
    path('retailers/', RetailerViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        })),
    path('retailers/<int:pk>/', RetailerViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })),
    path('delivery_partners/', DeliveryPartnerViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        })),
    path('delivery_partners/<int:id>/', DeliveryPartnerViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })),
    path('customers/', CustomerViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        })),
    path('customers/<int:id>/', CustomerViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })),
    path('products/', ProductViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        })),
    path('products/<int:id>/', ProductViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })),
    path('orders/', OrderViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        })),
    path('orders/<int:id>/', OrderViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })),
]
