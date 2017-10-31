from .settings import *  # noqa
from .settings import root

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

MEDIA_ROOT = (root - 4)('test_media')
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
