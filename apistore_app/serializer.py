from rest_framework import serializers, viewsets, decorators
from .models import items
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ItemtSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ["item", "item_category", "quantity", "price"]
        authentication_classes = [BasicAuthentication]
        permission_classes = [IsAuthenticated]

