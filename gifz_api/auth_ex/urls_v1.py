from django.conf.urls import (
    include,
    url,
)
from rest_framework import routers

from .views import UserViewSet


router = routers.DefaultRouter()
router.register(
    r'users',
    UserViewSet,
    base_name='user',
)


urlpatterns = [
    url(
        r'^',
        include(router.urls),
    ),
]
