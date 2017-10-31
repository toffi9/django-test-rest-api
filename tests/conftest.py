from django.contrib.auth import get_user_model

import pytest


@pytest.fixture()
def simple_user():
    return get_user_model().objects.create_user(
        username='t.lee',
        email='t.lee@gmail.co.uk',
        first_name='Tommy IV',
        last_name='Lee',
        is_active=True,
    )
