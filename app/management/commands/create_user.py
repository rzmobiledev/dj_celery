import os
from dotenv import load_dotenv
from psycopg2.errors import UniqueViolation
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from app.models import User


load_dotenv()


class Command(BaseCommand):

    def create_superuser(
            self,
            username: str,
            password: str,
            email: str,
            first_name: str,
            last_name: str
    ) -> User:

        return User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

    def handle(self, *args, **options) -> str | None:
        self.stdout.write("Creating new superuser...")
        username = os.environ.get('USERNAME')
        password = os.environ.get('PASSWORD')
        email = os.environ.get('EMAIL')
        first_name = os.environ.get('FIRST_NAME')
        last_name = os.environ.get('LAST_NAME')

        try:
            self.create_superuser(
                username, password, email, first_name, last_name)
        except UniqueViolation:
            self.stdout.write(
                "Email or username is already exists. Migration skipped.")
        except IntegrityError as e:
            self.stdout.write(str(e))
