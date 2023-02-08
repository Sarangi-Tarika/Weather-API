from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Weather, Stats
from .serializers import WeatherSerializers, StatsSerializers


class Weather(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializers
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date", "station_name"]


class Stats(generics.ListAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializers
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date", "station_name"]
