from rest_framework import viewsets

from .models import GIFEntry
from .serializers import GIFEntrySerializer


class GIFEntryViewSet(viewsets.ModelViewSet):

    queryset = GIFEntry.objects.select_related(
        'author',
    ).prefetch_related(
        'tags',
    )
    serializer_class = GIFEntrySerializer
