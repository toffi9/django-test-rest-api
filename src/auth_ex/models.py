from django.contrib.auth.models import (
    AbstractUser,
    UserManager,
)
from django.utils.translation import ugettext_lazy as _


class UserManager(UserManager):
    pass


class User(AbstractUser):

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
