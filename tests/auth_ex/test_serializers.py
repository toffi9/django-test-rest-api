import pytest
from mixer.backend.django import mixer

from auth_ex.models import User
from auth_ex.serializers import UserSerializer


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
        user = mixer.blend(
            User,
            username=user_data['username'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            is_active=user_data['is_active'],
        )

        serialized_user = UserSerializer(user).data
        assert serialized_user == user_data
