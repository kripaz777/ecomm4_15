from django.contrib.auth.models import User
from rest_framework import  viewsets
from .serializers import *

import django_filters.rest_framework
from .serializers import *
from rest_framework import generics
# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]