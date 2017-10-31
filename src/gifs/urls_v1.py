from django.conf.urls import url, include
from rest_framework import routers

from .views import GIFEntryViewSet

router = routers.DefaultRouter()
router.register(
    r'gifs',
    GIFEntryViewSet,
    base_name='gif',
)


urlpatterns = [
    url(
        r'^',
        include(router.urls),
    ),
]
