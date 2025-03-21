from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from product.choices import PlantSizeChoices
from product.models import Plant, Category
from rest_framework.views import APIView
from product.filters import PlantFilter
from product.serializers import PlantSerializer, CategorySerializer
from django.db.models import Count


class PlantListAPIView(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSizeChoices

class PlantDetailAPIView(generics.RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSizeChoices
    lookup_field = 'id'


class PlantAPIView(APIView):
    def get(self, request):
        plants = Plant.objects.all()
        plant_filter = PlantFilter(request.GET, queryset=plants)
        if plant_filter.is_valid():
            plants = plant_filter.qs
        paginator = PageNumberPagination()
        paginated_plants = paginator.paginate_queryset(plants, request)
        serializer = PlantSerializer(paginated_plants, many=True)
        return paginator.get_paginated_response(serializer.data)


class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.annotate(product_count=Count('plants'))
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

