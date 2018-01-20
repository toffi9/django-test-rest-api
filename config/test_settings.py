from .settings import *  # noqa
from .settings import root, INSTALLED_APPS

INSTALLED_APPS = [
    app for app in INSTALLED_APPS
    if app != 'cachalot'
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

MEDIA_ROOT = (root - 3)('test_media')
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
CACHALOT_ENABLED = False
