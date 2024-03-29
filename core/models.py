# Create your models here.
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.manager import BaseManager


class BaseModel(models.Model):
    """
        This model mixin usable for logical delete and logical activate status datas.
    """
    created = models.DateTimeField(auto_now_add=True, editable=False, )
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    delete_timestamp = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(
        null=True, blank=True,
        verbose_name=_("Deleted Datetime"),
        help_text=_("This is deleted datetime")
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_("Deleted status"),
        help_text=_("This is deleted status")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active status"),
        help_text=_("This is active status")
    )

    # custom manager for get active items
    objects = BaseManager()

    class Meta:
        abstract = True

    def deleter(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()


class BaseUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields["phone"]
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields["phone"]
        return super().create_user(username, email, password, **extra_fields)


class IpManagerDb(models.Model):
    ip = models.CharField(max_length=16, unique=True, verbose_name=_("Ip"))
    country = models.CharField(max_length=32, unique=False, verbose_name=_("Country"))
    city = models.CharField(max_length=32, unique=False, verbose_name=_("City"))
    lat = models.CharField(max_length=32, unique=False, verbose_name=_("Lat"))
    lon = models.CharField(max_length=32, unique=False, verbose_name=_("Lon"))
    views = models.IntegerField(default=0, verbose_name=_("Views"))
    access = models.BooleanField(default=True, verbose_name=_("Access"))

    class Meta:
        verbose_name = _("IpManagerDb")
        verbose_name_plural = _("IpsManagerDb")


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    objects = BaseUserManager()
    USERNAME_FIELD = "phone"
