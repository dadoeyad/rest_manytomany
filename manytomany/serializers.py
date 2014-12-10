from rest_framework import serializers

from .models import Property
from .models import PropertyImage


class PropertyImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyImage


class PropertyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
