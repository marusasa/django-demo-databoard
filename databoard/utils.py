import datetime
import time
import random
from django.utils import timezone

def generate_redondo_beach_temperature_data(year=2024):
    """
    Generates realistic hourly temperature data for Redondo Beach, CA for a given year.

    Args:
        year (int): The year for which to generate data.

    Returns:
        list: A list of tuples, where each tuple contains (datetime, temperature).
    """

    redondo_beach_temps = []
    start_date = datetime.datetime(year, 1, 1, 0, 0, 0, tzinfo=timezone.get_current_timezone())
    end_date = datetime.datetime(year + 1, 1, 1, 0, 0, 0, tzinfo=timezone.get_current_timezone())
    current_date = start_date

    # Average monthly temperatures for Redondo Beach (approximate)
    monthly_averages = {
        1: 57, 2: 58, 3: 59, 4: 61, 5: 64, 6: 67,
        7: 70, 8: 71, 9: 70, 10: 67, 11: 62, 12: 58,
    }

    while current_date < end_date:
        month = current_date.month
        average_temp = monthly_averages[month]

        # Add some daily variation
        daily_variation = random.uniform(-5, 5)

        # Add hourly variation (diurnal cycle)
        hour = current_date.hour
        diurnal_variation = 0
        if 6 <= hour < 18:  # Daytime, peak around 2-3 PM
            diurnal_variation = random.uniform(0, 8) * (1 - abs(14 - hour) / 8) # parabolic shape to diurnal variation.
        else: # nighttime, lower temps
            diurnal_variation = random.uniform(-4, 0) * (abs(hour-2)/12 if hour > 12 else abs(hour-14)/12) # parabolic shape to diurnal variation, lower at night.

        temperature = average_temp + daily_variation + diurnal_variation
        temperature = round(temperature, 1)  # Round to one decimal place

        redondo_beach_temps.append((current_date, temperature))
        
        # Handle Daylight Saving Time transitions
        next_hour = current_date + datetime.timedelta(hours=1)
        #compare epoch time
        if time.mktime(next_hour.timetuple()) == time.mktime(current_date.timetuple()): #repeated time
            current_date += datetime.timedelta(hours=2) #skip the repeated hour
        else:
            current_date = next_hour

    return redondo_beach_temps

# Example usage (to save to a list or database):
#temperature_data = generate_redondo_beach_temperature_data()

# Example of how to print the first 10 entries:
#for i in range(10):
#    print(temperature_data[i])

# Example of how to use the data in a Django model (assuming you have a Temperature model):
"""
from your_app.models import Temperature

for timestamp, temp in temperature_data:
    Temperature.objects.create(timestamp=timestamp, temperature=temp)
"""


def generate_redondo_beach_pressure_data(year=2024):
    """
    Generates realistic hourly barometric pressure data for Redondo Beach, CA for a given year,
    handling Daylight Saving Time to prevent repeated timestamps.

    Args:
        year (int): The year for which to generate data.

    Returns:
        list: A list of tuples, where each tuple contains (datetime, pressure).
    """

    redondo_beach_pressures = []
    start_date = datetime.datetime(year, 1, 1, 0, 0, 0, tzinfo=timezone.get_current_timezone())
    end_date = datetime.datetime(year + 1, 1, 1, 0, 0, 0, tzinfo=timezone.get_current_timezone())
    current_date = start_date

    # Average barometric pressure for Redondo Beach (approximate, in millibars/hectopascals)
    # Average sea level pressure is around 1013.25 hPa. Redondo beach is close to sea level.
    average_pressure = 1013.25

    # Add some seasonal and daily variation
    while current_date < end_date:
        # Seasonal variation (slight, higher in winter)
        month = current_date.month
        seasonal_variation = random.uniform(-1, 1) * (1 if month in [12, 1, 2] else -1 if month in [6,7,8] else 0)

        # Daily variation (diurnal cycle, slight)
        hour = current_date.hour
        diurnal_variation = random.uniform(-0.5, 0.5) * (1 if (hour in [10, 22]) else -1 if hour in [4,16] else 0) #Slight peaks around 10am and 10pm, slight lows around 4am and 4pm.
        #Random small variations.
        random_variation = random.uniform(-2,2)

        pressure = average_pressure + seasonal_variation + diurnal_variation + random_variation
        pressure = round(pressure, 2)  # Round to two decimal places

        redondo_beach_pressures.append((current_date, pressure))

        # Handle Daylight Saving Time transitions
        next_hour = current_date + datetime.timedelta(hours=1)
        #compare epoch time
        if time.mktime(next_hour.timetuple()) == time.mktime(current_date.timetuple()): #repeated time
            current_date += datetime.timedelta(hours=2)
        else:
            current_date = next_hour

    return redondo_beach_pressures

# Example usage (to save to a list or database):
#pressure_data = generate_redondo_beach_pressure_data()

# Example of how to print the first 10 entries:
#for i in range(10):
#    print(pressure_data[i])

# Example of how to use the data in a Django model (assuming you have a Pressure model):
"""
from your_app.models import Pressure

for timestamp, pressure in pressure_data:
    Pressure.objects.create(timestamp=timestamp, pressure=pressure)
"""


def generate_redondo_beach_humidity_data(year=2024):
    """
    Generates realistic hourly humidity data for Redondo Beach, CA for a given year,
    handling Daylight Saving Time to prevent repeated timestamps.

    Args:
        year (int): The year for which to generate data.

    Returns:
        list: A list of tuples, where each tuple contains (datetime, humidity).
    """

    redondo_beach_humidities = []
    start_date = datetime.datetime(year, 1, 1, 0, 0, 0, tzinfo=timezone.get_current_timezone())
    end_date = datetime.datetime(year + 1, 1, 1, 0, 0, 0, tzinfo=timezone.get_current_timezone())
    current_date = start_date

    # Average humidity for Redondo Beach (approximate percentage)
    # Redondo beach is near the coast, so humidity is relatively high.
    average_humidity = 70

    while current_date < end_date:
        # Seasonal variation (slightly higher in winter)
        month = current_date.month
        seasonal_variation = random.uniform(-5, 5) * (1 if month in [12, 1, 2] else -0.5 if month in [6, 7, 8] else 0)

        # Daily variation (higher at night, lower during the day)
        hour = current_date.hour
        diurnal_variation = random.uniform(-10, 10) * (1 - abs(12 - hour) / 12)  # Inverted parabolic shape

        # Random small variations
        random_variation = random.uniform(-5, 5)

        humidity = average_humidity + seasonal_variation + diurnal_variation + random_variation
        humidity = max(0, min(100, round(humidity)))  # Clamp to 0-100%

        redondo_beach_humidities.append((current_date, humidity))

        # Handle Daylight Saving Time transitions
        next_hour = current_date + datetime.timedelta(hours=1)
        if time.mktime(next_hour.timetuple()) == time.mktime(current_date.timetuple()): #repeated time
            current_date += datetime.timedelta(hours=2)
        else:
            current_date = next_hour

    return redondo_beach_humidities