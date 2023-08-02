from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
class ProductApiView(APIView):
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()

        data = {
            'products' : ProductSerializer(products, many = True).data
        }
        
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        product_name = request.data['name']
        product_description = request.data['description']
        product_price = request.data['price']

        product_category = Category.objects.get(pk=request.data['category'])

        new_product = Product(
            name = product_name,
            description = product_description,
            price = product_price,
            category = product_category
        )
        new_product.save()

        return Response({'message': 'Product created'}, status=status.HTTP_201_CREATED)


class ProductDetailApiView(APIView):
    permission_classes = []

    def get(self, request):
        product_id = request.GET.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        
        data = {
            'product' : ProductSerializer(product).data
        }

        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request):
        product_id = request.data['product_id']
        product = Product.objects.filter(pk=product_id)

        if product:
            product[0].delete()
            return Response({'message': 'Product is deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        product_id = request.data['product_id']
        product = Product.objects.filter(pk=product_id)

        if product:
            serializer = ProductSerializer(product[0], data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Product is updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Wrong keys!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Produuct not found'}, status=status.HTTP_400_BAD_REQUEST)