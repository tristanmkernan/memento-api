import pytest

from django.test.client import Client
from rest_framework_simplejwt.tokens import SlidingToken

from myauth.models import User


@pytest.fixture
def user(db):
    user = User.objects.create_user(username="thedude", password="abides")

    return user


@pytest.fixture
def authenticated_client(user):
    token = SlidingToken.for_user(user)
    client = Client(HTTP_AUTHORIZATION=f"Bearer {str(token)}")
    return client
