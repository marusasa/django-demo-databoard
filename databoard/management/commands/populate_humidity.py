from django.core.management.base import BaseCommand
from databoard.models import Humidity
from databoard.utils import generate_redondo_beach_humidity_data

class Command(BaseCommand):
    help = 'Populates the Humidity model with Redondo Beach data.'

    def handle(self, *args, **options):
        humidity_data = generate_redondo_beach_humidity_data()
        for timestamp, humidity in humidity_data:
            Humidity.objects.create(timestamp=timestamp, humidity=humidity)
        self.stdout.write(self.style.SUCCESS('Humidity data populated successfully.'))