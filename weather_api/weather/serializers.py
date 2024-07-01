from rest_framework import serializers
from .models import WeatherRecord, WeatherStats

class WeatherRecordSerializer(serializers.ModelSerializer):
    """ Serializer for converting WeatherRecord model instances to/from JSON """
    class Meta:
        model = WeatherRecord
        fields = '__all__'

class WeatherStatsSerializer(serializers.ModelSerializer):
    """ Serializer for converting WeatherStats model instances to/from JSON """
    class Meta:
        model = WeatherStats
        fields = '__all__'
