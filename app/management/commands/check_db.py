from psycopg2 import OperationalError as PgError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    """Check database is ready"""

    def handle(self, *args, **options) -> str | None:
        self.stdout.write("Waiting database ready...")
        ready = False

        while not ready:
            try:
                self.check(databases=["default"])
                ready = True
            except (PgError, OperationalError):
                self.stdout.write("waiting for 1 second...")
                time.sleep(1)
        self.stdout.write("YOUR DATABASE IS READY!")
