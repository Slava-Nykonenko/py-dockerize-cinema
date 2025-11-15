import time

from dotenv import load_dotenv
from django.core.management import BaseCommand
from django.db import connections
from django.db import OperationalError

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                _ = connections["default"]
                return "Successfully connected to PostgreSQL"
            except OperationalError:
                time.sleep(1)
                print("Waiting for connection to the PostgreSQL database...")
