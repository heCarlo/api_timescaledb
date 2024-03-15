from rest_framework import serializers
from ..models.weatherEntity import WeatherEntity

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherEntity
        fields = ['datetime', 'code', 'direction', 'temperature', 'rh', 'pressure', 'precip', 'prmsl', 'tmpsrf', 'vel_gfs', 'vel_twr']
