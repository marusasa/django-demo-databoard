# databoard/management/commands/populate_temperatures.py
from django.core.management.base import BaseCommand
from databoard.models import Temperature
from databoard.utils import generate_redondo_beach_temperature_data #create utils.py with the function.

class Command(BaseCommand):
    help = 'Populates the Temperature model with Redondo Beach data.'

    def handle(self, *args, **options):
        temperature_data = generate_redondo_beach_temperature_data()
        for timestamp, temp in temperature_data:
            self.stdout.write(f"{timestamp} {temp}")
            Temperature.objects.create(timestamp=timestamp, temperature=temp)
        self.stdout.write(self.style.SUCCESS('Temperature data populated successfully.'))