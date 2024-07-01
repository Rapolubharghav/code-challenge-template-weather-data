from django.apps import AppConfig


class WeatherConfig(AppConfig):

    # Define the default primary key field for models in this app
    default_auto_field = 'django.db.models.BigAutoField'

    # Set the name of the app
    name = 'weather'
