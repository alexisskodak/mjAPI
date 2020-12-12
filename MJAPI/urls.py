from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('contacts', viewset=ContactViewSet)
router.register('retailers', viewset=RetailerViewSet)
router.register('delivery-partners', viewset=DeliveryPartnerViewSet)
router.register('customers', viewset=CustomerViewSet)
router.register('products', viewset=ProductViewSet)
router.register('orders', viewset=OrderViewSet)

urlpatterns = router.urls
