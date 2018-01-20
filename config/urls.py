from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.documentation import include_docs_urls


app_urls_modules_v1 = [
    'gifz_api.auth_ex.urls_v1',
    'gifz_api.gifs.urls_v1',
]

app_urls_v1 = [
    url(r'', include(app_urls_module))
    for app_urls_module in app_urls_modules_v1
]

urlpatterns = [
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
            include_docs_urls(title='API'),
        ),
    ]

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
