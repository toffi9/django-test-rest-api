import pytest
from rest_framework.test import APIClient


class UserViewSetTest:

    @pytest.fixture(scope='class')
    def url(self):
        return '/api/v1/users/'

    @pytest.mark.django_db
    def test_list(self, url, list_of_5_users):
        client = APIClient()
        client.force_authenticate(user=list_of_5_users[0])

        response = client.get(url)
        assert len(response.data['results']) == 5
