from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .serializers import PropertyCreateSerializer


from .models import Property


class PropertyViewSet(viewsets.ModelViewSet):

    queryset = Property.objects.all()
    serializer_class = PropertyCreateSerializer
    authentication_classes = (TokenAuthentication,)
