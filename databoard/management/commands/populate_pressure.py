# databoard/management/commands/populate_pressure.py
from django.core.management.base import BaseCommand
from databoard.models import BarometricPressure
from databoard.utils import generate_redondo_beach_pressure_data #assuming you put the pressure function in utils.py

class Command(BaseCommand):
    help = 'Populates the BarometricPressure model with Redondo Beach data.'

    def handle(self, *args, **options):
        pressure_data = generate_redondo_beach_pressure_data()
        for timestamp, pressure in pressure_data:
            BarometricPressure.objects.create(timestamp=timestamp, pressure=pressure)
        self.stdout.write(self.style.SUCCESS('Barometric pressure data populated successfully.'))