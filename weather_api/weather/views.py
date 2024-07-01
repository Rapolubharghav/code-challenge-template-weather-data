from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import WeatherRecord, WeatherStats
from .serializers import WeatherRecordSerializer, WeatherStatsSerializer

# Pagination class for WeatherRecord
class WeatherRecordPagination(PageNumberPagination):
    page_size = 10  # You can adjust this value as needed
    page_size_query_param = 'page_size'
    max_page_size = 100

# API view for listing WeatherRecord objects
class WeatherRecordList(generics.ListAPIView):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer
    pagination_class = WeatherRecordPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['station_id', 'date']

# Pagination class for WeatherStats
class WeatherStatsPagination(PageNumberPagination):
    page_size = 10  # You can adjust this value as needed
    page_size_query_param = 'page_size'
    max_page_size = 100

# API view for listing WeatherStats objects
class WeatherStatsList(generics.ListAPIView):
    queryset = WeatherStats.objects.all()
    serializer_class = WeatherStatsSerializer
    pagination_class = WeatherStatsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['station_id', 'year']
