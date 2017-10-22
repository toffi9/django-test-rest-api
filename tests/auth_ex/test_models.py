import pytest
from mixer.backend.django import mixer


class UserManagerTest:
    pass


class UserTest:

    @pytest.mark.django_db
    def test_full_name(self):
        user = mixer.blend(
            'auth_ex.User',
            first_name='Tommy IV',
            last_name='Lee',
        )
        assert user.full_name == 'Tommy IV Lee'
