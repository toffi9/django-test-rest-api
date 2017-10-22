from django.conf.urls import url, include

import gifs.urls


apps_urls_modules = [
    gifs.urls,
]

app_urls = [
    url(r'', include(app_urls_module, namespace='v1'))
    for app_urls_module in apps_urls_modules
]

urlpatterns = [
    url(
        r'^',
        include(app_urls),
    ),
]
