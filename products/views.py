from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache


class ProductListAPIView(APIView):

    def get(self, request):
        cache_key = 'product_list'

        if not cache.get(cache_key):
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            cache.set(cache_key, serializer.data, 10)

        response_data = cache.get(cache_key)
        return Response(response_data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)