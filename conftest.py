import pytest
from dotenv import load_dotenv
from faker import Faker
from django.core.management import call_command
from pytest_django.plugin import _DatabaseBlocker
from app.models import User
from dataclasses import asdict, dataclass

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def django_db_setup(django_db_setup: None, django_db_blocker: _DatabaseBlocker | None):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data.json')


fake = Faker()


@dataclass
class TempUser:
    password: str = fake.password()
    email: str = fake.email()
    username: str = email.replace('@', '_').replace('.', '_')
    first_name: str = fake.first_name()
    last_name: str = fake.last_name()

    def json(self) -> dict:
        return asdict(self)


@pytest.fixture
def random_password() -> str:
    return fake.password()


@pytest.fixture
def registered_user(db: None):
    json_data = TempUser()
    user = User.objects.create_user(**json_data.json())
    return user


@pytest.fixture
def raw_user_data():
    return TempUser()
