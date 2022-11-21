from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from product.serializers.product_serializer import ProductSerializer


class OrderViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    @property
    def get_queryset(self):
        return Order.objects.all().order_by("id")
