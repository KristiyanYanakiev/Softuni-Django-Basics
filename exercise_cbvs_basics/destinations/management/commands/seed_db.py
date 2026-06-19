from django.core.management.base import BaseCommand
from destinations.factories import DestinationFactory


class Command(BaseCommand):
    help = 'Seeds the database with 25 highly realistic destinations using factory_boy'

    def handle(self, *args, **options):
        self.stdout.write("Clearing existing destination data...")
        # Optional: uncomment the line below if you want a clean slate every time you seed
        # Destination.objects.all().delete()

        self.stdout.write("Planting test seeds...")

        # This single line handles the entire database loop for you!
        DestinationFactory.create_batch(25)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database with 25 destinations! 🎉"))