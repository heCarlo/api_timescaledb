from rest_framework import viewsets
from ..models.weatherEntity import WeatherEntity
from ..serializers.weatherSerializer import WeatherDataSerializer

class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherEntity.objects.order_by('-id')[:1]
    serializer_class = WeatherDataSerializer
