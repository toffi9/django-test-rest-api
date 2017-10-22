from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls


app_urls_modules_v1 = [
    'auth_ex.urls_v1',
    # gifs.urls,
]

app_urls_v1 = [
    url(r'', include(app_urls_module))
    for app_urls_module in app_urls_modules_v1
]

urlpatterns = [
    url(
        r'^jet/',
        include('jet.urls', 'jet'),
    ),
    url(
        r'^admin/',
        admin.site.urls,
    ),
    url(
        r'^api/v1/',
        include(app_urls_v1, 'v1'),
    ),
]

if settings.DEBUG:

    import debug_toolbar
    urlpatterns += [
        url(
            r'^__debug__/',
            include(debug_toolbar.urls),
        ),
        url(
            r'^api-auth/',
            include(
                'rest_framework.urls',
                namespace='rest_framework',
            ),
        ),
        url(
            r'^docs/',
            include_docs_urls(title='Gifz API'),
        ),
    ]
