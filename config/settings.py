import environ
import raven


root = environ.Path(__file__)
env = environ.Env()

BASE_DIR = root()

DEBUG = env('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
SITE_ID = env('SITE_ID', default=1)
SECRET_KEY = env('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'stdimage',
    'django_cleanup',
    'taggit',
    'taggit_serializer',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'raven.contrib.django.raven_compat',
    'cachalot',

    'gifz_api.auth_ex',
    'gifz_api.gifs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True,
    }

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': env.db(
        default='postgres://postgres:postgres@postgres:5432/postgres',
    ),
}

AUTH_USER_MODEL = 'auth_ex.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa: E501
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = env('STATIC_URL', default='/static/')
STATIC_ROOT = env('STATIC_ROOT', default=(root - 3)('static_files'))

MEDIA_URL = env('MEDIA_URL', default='/media/')
MEDIA_ROOT = env('MEDIA_ROOT', default=(root - 3)('media_files'))

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',  # noqa: E501
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',  # noqa: E501
    'PAGE_SIZE': 25,
}

GIFS_PAGE_SIZE = env('GIFS_PAGE_SIZE', default=40)

# --- CACHE ---
CACHES = {
    'default': env.cache(
        default='redis://redis:6379/1?client_class=django_redis.client.DefaultClient',  # noqa: E501
    ),
}
CACHALOT_ENABLED = env.bool('CACHALOT_ENABLED', default=False)
CACHALOT_TIMEOUT = env('CACHALOT_TIMEOUT', default=60*20)

SENTRY_ENABLED = env.bool('SENTRY_ENABLED', default=False)
if SENTRY_ENABLED:
    RAVEN_CONFIG = {
        'dsn': env('RAVEN_DSN'),
        'release': raven.fetch_git_sha((root - 2)()),
    }

CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST', default=[])
