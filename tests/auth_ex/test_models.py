import pytest


class UserManagerTest:

    pass


class UserTest:

    @pytest.mark.django_db
    def test_full_name(self, simple_user):
        assert simple_user.full_name == 'Tommy IV Lee'
