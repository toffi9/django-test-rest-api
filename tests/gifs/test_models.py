import pytest
from django.conf import settings
from mixer.backend.django import mixer

from gifs.models import GIFEntry


class GIFEntryTest:

    @pytest.mark.django_db
    def test_has_proper_fields(self):
        gif_entry = GIFEntry()
        gif_entry.title = 'Funny Cats'
        gif_entry.gif_file = None
        gif_entry.author = mixer.blend(
            settings.AUTH_USER_MODEL,
            is_active=True,
            is_superuser=False,
        )
        gif_entry.save()
        gif_entry.tags.add('funny', 'cats')

        assert gif_entry.pk is not None

    @pytest.mark.django_db
    def test_str(self):
        gif_entry = mixer.blend(
            GIFEntry,
            title='Funny Vines',
        )

        assert str(gif_entry) == 'Funny Vines'
