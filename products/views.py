import datetime

from django.db.models import Sum
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Batch
from .serializers import ProductSerializer, BatchSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BatchList(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


class BatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


@api_view(['GET'])
def product_batches(request, pk):
    """
    Retrieve product batch information.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        batches = Batch.objects.filter(product=product).order_by('expires_on').all()
        serializer = BatchSerializer(batches, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def product_inventory(request, pk):
    """
    Retrieve product inventory information.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        today = datetime.date.today()
        amounts = {
            'fresh': Batch.objects.filter(product=product, expires_on__gt=today).aggregate(Sum('amount'))['amount__sum'] or 0,
            'expiring_today': Batch.objects.filter(product=product, expires_on=today).aggregate(Sum('amount'))['amount__sum'] or 0,
            'expired': Batch.objects.filter(product=product, expires_on__lt=today).aggregate(Sum('amount'))['amount__sum'] or 0,
        }
        return Response(amounts)
