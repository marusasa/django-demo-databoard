from django.db import models


class Temperature(models.Model):
    timestamp = models.DateTimeField(unique=True)
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.timestamp}: {self.temperature}°F"
        
        
class BarometricPressure(models.Model):
    """
    Model to store barometric pressure data.
    """
    timestamp = models.DateTimeField(unique=True, help_text="Timestamp of the pressure reading.")
    pressure = models.FloatField(help_text="Barometric pressure in hectopascals (hPa).")

    def __str__(self):
        return f"{self.timestamp}: {self.pressure} hPa"

    class Meta:
        verbose_name = "Barometric Pressure"
        verbose_name_plural = "Barometric Pressures"
        ordering = ['timestamp']    
        
class Humidity(models.Model):
    """
    Model to store humidity data.
    """
    timestamp = models.DateTimeField(unique=True, help_text="Timestamp of the humidity reading.")
    humidity = models.IntegerField(help_text="Relative humidity as a percentage (0-100).")

    def __str__(self):
        return f"{self.timestamp}: {self.humidity}%"

    class Meta:
        verbose_name = "Humidity"
        verbose_name_plural = "Humidities"
        ordering = ['timestamp']
