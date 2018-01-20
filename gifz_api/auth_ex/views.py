from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.filter(
        is_superuser=False,
    )
    serializer_class = UserSerializer
