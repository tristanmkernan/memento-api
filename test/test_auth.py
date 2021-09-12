import pytest

from django.urls.base import reverse
from rest_framework import status

from myauth.models import User


@pytest.mark.django_db
def test_login_or_signup(client):
    username = "thedude"
    password = "abides"

    payload = {
        "username": username,
        "password": password
    }

    response = client.post(reverse("myauth-login-or-signup"), payload)

    assert response.status_code == status.HTTP_200_OK

    assert "token" in response.data
    assert "username" in response.data

    user = User.objects.get(username=username)

    # now attempt to log in with same credentials
    response = client.post(reverse("myauth-login-or-signup"), payload)

    assert response.status_code == status.HTTP_200_OK

    assert "token" in response.data
    assert "username" in response.data

    potential_other_user = User.objects.get(username=username)

    assert user == potential_other_user, "Login performed registration"
