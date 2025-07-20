from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with Listings'

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(username='demo_user')
        sample_data = [
            {'title': 'Cozy Apartment', 'description': 'A nice place.', 'location': 'Alexandria', 'price_per_night': 80},
            {'title': 'Beach House', 'description': 'By the sea.', 'location': 'Agami', 'price_per_night': 120},
            # Add as many as needed
        ]
        for data in sample_data:
            Listing.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'location': data['location'],
                    'price_per_night': data['price_per_night'],
                    'owner': user
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded Listings!'))
