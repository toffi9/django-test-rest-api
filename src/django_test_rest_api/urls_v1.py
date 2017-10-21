from django.conf.urls import url, include


apps_urls_modules = [
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
