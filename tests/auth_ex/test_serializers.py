import pytest

from gifz_api.auth_ex.models import User
from gifz_api.auth_ex.serializers import UserSerializer


class UserSerializerTest:

    @pytest.mark.django_db
    def test_data(self):
        user_data = {
            'pk': 1,
            'username': 'normon',
            'first_name': 'Norman',
            'last_name': 'Freeman',
            'email': 'n.freeman@gmail.co.uk',
            'is_active': True,
        }
        user = User.objects.create_user(
            **user_data,
        )

        serialized_user = UserSerializer(user).data
        assert serialized_user == user_data
