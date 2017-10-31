import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

import pytest
from gifs.models import GIFEntry


class UUID4Monkey(object):
    hex = '653d1c6863404b9689b75fa930c9d0a0'


GIFS_DIR = os.path.join(settings.MEDIA_ROOT, 'gifs')


@pytest.fixture()
def gif_file():
    file_path = './tests/fixtures/funny_cat.gif'

    with open(file_path, 'rb') as f:
        f.seek(0)
        gif = SimpleUploadedFile(f.name, f.read())

    yield gif

    gif.close()

    file_path_after_storage_save = os.path.join(
        GIFS_DIR,
        '{}.gif'.format(UUID4Monkey.hex),
    )
    os.remove(file_path_after_storage_save)


@pytest.fixture()
def gif_entry(simple_user, gif_file):
    gif_entry = GIFEntry(
        title='Funny Vines',
        author=simple_user,
        gif_file=gif_file,
    )
    gif_entry.save()

    return gif_entry
