from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from app.models import User


class RestClientAPI:
    api = APIClient()

    def access_token(self, user: User):
        token = RefreshToken.for_user(user)
        return token.access_token
