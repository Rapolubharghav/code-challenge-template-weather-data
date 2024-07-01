from django.test import TestCase
from .models import WeatherRecord, WeatherStats

class WeatherRecordTestCase(TestCase):
    def setUp(self):
        WeatherRecord.objects.create(station_id="001", date="2024-06-28", max_temp=30, min_temp=20, precipitation=5)
        WeatherRecord.objects.create(station_id="002", date="2024-06-28", max_temp=32, min_temp=22, precipitation=7)

    def test_weather_record(self):
        record1 = WeatherRecord.objects.get(station_id="001", date="2024-06-28")
        record2 = WeatherRecord.objects.get(station_id="002", date="2024-06-28")
        self.assertEqual(record1.max_temp, 30)
        self.assertEqual(record1.min_temp, 20)
        self.assertEqual(record1.precipitation, 5)
        self.assertEqual(record2.max_temp, 32)
        self.assertEqual(record2.min_temp, 22)
        self.assertEqual(record2.precipitation, 7)

class WeatherStatsTestCase(TestCase):
    def setUp(self):
        WeatherStats.objects.create(station_id="001", year=2024, avg_max_temp=30, avg_min_temp=20, total_precipitation=5)

    def test_weather_stats(self):
        stats = WeatherStats.objects.get(station_id="001", year=2024)
        self.assertEqual(stats.avg_max_temp, 30)
        self.assertEqual(stats.avg_min_temp, 20)
        self.assertEqual(stats.total_precipitation, 5)
