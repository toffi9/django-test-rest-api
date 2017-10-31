import os
import uuid

import pytest
from gifs.models import GIFEntry

from .conftest import GIFS_DIR, UUID4Monkey

uuid.__dict__['uuid4'] = lambda: UUID4Monkey()


class GIFEntryTest:

    @pytest.mark.django_db
    def test_has_proper_fields(self, gif_file, simple_user):
        gif_entry = GIFEntry()
        gif_entry.title = 'Funny Cats'
        gif_entry.gif_file = gif_file
        gif_entry.author = simple_user
        gif_entry.save()
        gif_entry.tags.add('funny', 'cats')

        assert GIFEntry.objects.count() == 1
        assert GIFEntry.objects.get(pk=1) == gif_entry

    @pytest.mark.django_db
    def test_if_file_is_uploaded_properly(self, gif_entry):
        file_path = os.path.join(GIFS_DIR, '{}.gif'.format(UUID4Monkey.hex))
        assert os.path.exists(file_path)

        with open(file_path, 'rb') as f:
            gif_entry.gif_file.seek(0)
            assert gif_entry.gif_file.read() == f.read()

    @pytest.mark.django_db
    def test_gif_file_is_required(self, simple_user):
        gif_entry = GIFEntry(
            title='Super gif',
            author=simple_user,
        )

        # with pytest.raises():
        gif_entry.save()

    # def test_if_jpeg_cant_be_passed(self, jpeg_file):

    # def test_if_txt_cant_be_passed(self, txt_file):

    @pytest.mark.django_db
    def test_str_of_object(self, gif_entry):
        assert str(gif_entry) == 'Funny Vines'
