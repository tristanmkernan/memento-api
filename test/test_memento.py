import pytest

from django.urls.base import reverse
from rest_framework import status


@pytest.mark.django_db
def test_retrieve_mementos(authenticated_client, user):

    response = authenticated_client.get(reverse("memento-list"))

    assert response.status_code == status.HTTP_200_OK
