import uuid
from urllib.parse import urljoin

from django.conf import settings

import pytest
from gifs.models import GIFEntry
from gifs.serializers import GIFEntrySerializer

from .conftest import UUID4Monkey

uuid.__dict__['uuid4'] = lambda: UUID4Monkey()


class GIFEntrySerializerTest:
    @pytest.mark.django_db
    def test_data(self, simple_user, gif_file):
        data = {
            'pk': 1,
            'title': 'GIFception',
            'gif_file': urljoin(
                settings.MEDIA_URL,
                'gifs/{}.gif'.format(UUID4Monkey.hex),
            ),
            'author': 1,
            'tags': [
                'funny',
                'cats',
            ],
        }

        create_data = data.copy()
        create_data.update({
            'gif_file': gif_file,
            'author': simple_user,
        })
        create_data.pop('tags')

        gif_entry = GIFEntry.objects.create(
            **create_data,
        )
        gif_entry.tags.add(*data['tags'])

        serialized_data = GIFEntrySerializer(gif_entry).data
        assert serialized_data == data
