from rest_framework import generics

from product.choices import PlantSizeChoices
from product.models import Plant


class PlantListAPIView(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSizeChoices


class PlantCreateAPIView(generics.CreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSizeChoices


class PlantUpdateAPIView(generics.UpdateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSizeChoices
    lookup_field = 'id'

class PlantDeleteAPIView(generics.DestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSizeChoices
    lookup_field = 'id'

class PlantDetailAPIView(generics.RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSizeChoices
    lookup_field = 'id'

class PlantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSizeChoices
    lookup_field = 'id'

class PlantDetailUpdateDeleteAPIView(generics.RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSizeChoices
    lookup_field = 'id'
