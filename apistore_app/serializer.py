from rest_framework import serializers, viewsets, decorators
from .models import items


class ItemtSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ["item", "item_category", "quantity", "price"]
        authentication_classes = [BasicAuthentication]
        permission_classes = [IsAuthenticated]

