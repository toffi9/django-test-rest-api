from django.contrib.auth.models import UserManager as DjangoUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class UserManager(DjangoUserManager):
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
