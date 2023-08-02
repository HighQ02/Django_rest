from rest_framework.serializers import ModelSerializer
from .models import *


class ProductSerializer(ModelSerializer):
    # Serializer - инструмент, которые конвертирует обычный query в json
    class Meta:
        model = Product
        fields = '__all__'
