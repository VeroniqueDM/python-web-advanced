from django.shortcuts import render
from rest_framework import generics as api_views
from rest_framework import mixins as api_mixins
from rest_framework import permissions
# from rest_framework import views as api_views
from rest_framework import serializers
from rest_framework.response import Response

from drf_demos.api.models import Product

# Create your views here.

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)
    # category = IdAndNameCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductsListView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    #
    # def list(self, request, *args, **kwargs):
    #     print(self.request.user)
    #     return super().list(request, *args, **kwargs)
    #
    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)
    #
    # # def get_queryset(self):

    def get(self, request):
        products =Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=False)
        if serializer.is_valid():
            print(serializer.validated_data)