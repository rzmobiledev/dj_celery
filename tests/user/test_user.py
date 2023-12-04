import pytest
from django.urls import reverse
from tests.rest_client import RestClientAPI
from app.models import User


@pytest.mark.django_db(databases=["default"])
class TestUser(RestClientAPI):
    """Test process CRUD client"""

    endpoint = reverse('token_obtain_pair')
    verify_endpoint = reverse('token_verify')

    def test_user_change_password(self, registered_user: User, random_password):
        user = registered_user
        user.set_password(random_password)
        user.save()
        assert user.check_password(random_password)

    def test_login_registered_user(self, registered_user: User, raw_user_data):
        user = raw_user_data
        self.api._credentials = {}
        response = self.api.post(path=self.endpoint, data=user.json())
        assert response.status_code == 200

    def test_login_registered_user_with_wrong_password(self, registered_user: User, raw_user_data):

        self.api._credentials = {}

        user = raw_user_data.json()
        user["password"] = "wrongpass1234"

        bad_response = self.api.post(
            path=self.endpoint, data=user)

        assert bad_response.status_code == 401

    def test_token_valid(self, registered_user: User, raw_user_data):
        self.api._credentials = {}
        token_response = self.api.post(
            path=self.verify_endpoint, data={"token": f"{self.access_token(registered_user)}"}, format="json")
        assert token_response.status_code == 200

    def test_token_invalid(self, registered_user: User, raw_user_data):
        self.api._credentials = {}
        token_response = self.api.post(
            path=self.verify_endpoint, data={"token": "be3857830sjinay&4jns432knsnfas"}, format="json")
        assert token_response.status_code == 401
