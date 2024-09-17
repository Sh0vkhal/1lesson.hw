from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Car
from .serializers import CarSerializer
# Create your views here.

class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetailAPIView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer