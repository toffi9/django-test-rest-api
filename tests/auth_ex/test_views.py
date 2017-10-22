import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient

from auth_ex.models import User


class UserViewSetTest:

    @pytest.fixture(scope='class')
    def url(self):
        return '/api/v1/users/'

    @pytest.mark.django_db
    def test_list(self, url):
        users = mixer.cycle(5).blend(User, is_superuser=False, is_active=True)

        client = APIClient()
        client.force_authenticate(user=users[0])

        response = client.get(url)
        assert len(response.data['results']) == 5
