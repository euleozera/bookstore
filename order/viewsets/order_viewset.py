from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSeralizer


class OrderViewSet(ModelViewSet):

    serializer_class = OrderSeralizer
    queryset = Order.objects.all().order_by("id")
