from django.core.management.base import BaseCommand

from strava.retrieve_club import retrieve_club


class Command(BaseCommand):
    def handle(self, *args, **options):
        retrieve_club()