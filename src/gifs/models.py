from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from stdimage.models import StdImageField
from taggit.managers import TaggableManager


class GIFEntry(TimeStampedModel):
    title = models.CharField(
        _('title'),
        max_length=255,
    )
    gif_file = StdImageField(
        # TODO: Special validator of filetype
        upload_to='path/to/img',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('author'),
        related_name='gif_entries',
        on_delete=models.CASCADE,
    )
    tags = TaggableManager()

    class Meta:
        verbose_name = _('')
        verbose_name_plural = _('')

    def __str__(self):
        return self.title
