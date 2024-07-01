from django.urls import path
from .views import WeatherRecordList, WeatherStatsList

urlpatterns = [
    path('weather/', WeatherRecordList.as_view(), name='Weather-Records-List'),
    path('weather/stats/', WeatherStatsList.as_view(), name='Weather-Statistics-List'),
]
