import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture()
def list_of_5_users():
    users = [
        {
            'username': 'TommyHilfingerIII',
            'email': 't.hilf@biz.net',
            'first_name': 'Tommy',
            'last_name': 'Hilfinger',
        },
        {
            'username': 'belluci',
            'email': 'luigi555@one.com',
            'first_name': 'Mario',
            'last_name': 'Bellucci',
        },
        {
            'username': 'tor',
            'email': 'onion@onion.dark.net',
            'first_name': 'Anonymous',
            'last_name': 'Anon',
        },
        {
            'username': 'ppp333',
            'email': 'ppp@gmail.com',
            'first_name': 'Mirko',
            'last_name': 'Rat',
        },
        {
            'username': 'pollak',
            'email': 'polishblood@terror.pl',
            'first_name': 'John',
            'last_name': 'Pollack',
        },
    ]

    users = [
        User(
            **user,
            is_active=True,
        )
        for user in users
    ]

    return User.objects.bulk_create(users)
