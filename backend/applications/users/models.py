import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import (
    FileExtensionValidator,
    MaxLengthValidator,
    MinLengthValidator,
)
from django.db import models
from django.utils import timezone
from django.utils.text import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

from applications.users.constants import (
    EMAIL_MAX_LENGTH,
    FIRST_NAME_MAX_LENGTH,
    LAST_NAME_MAX_LENGTH,
    RESTRICTED_USERNAMES,
    STATUS_MAX_LENGTH,
    USER_PHOTO_ALLOWED_EXTENSIONS,
    USER_PHOTO_QUALITY_PERCENT,
    USER_PHOTO_SIZE,
    USERNAME_MAX_LENGTH,
    USERNAME_MIN_LENGTH,
)
from applications.users.managers import UserManager
from applications.users.mixins import UserStatusMixin
from core.utils import UploadAndRenameImage
from core.validators import RestrictedUsernamesValidator, UsernameValidator


class User(AbstractBaseUser, PermissionsMixin, UserStatusMixin):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    id = models.UUIDField(
        _("User ID"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    email = models.EmailField(
        _("Email"),
        max_length=EMAIL_MAX_LENGTH,
        unique=True,
        db_index=True,
    )
    username = models.CharField(
        "Username",
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        db_index=True,
        validators=[
            UsernameValidator(),
            RestrictedUsernamesValidator(RESTRICTED_USERNAMES),
            MinLengthValidator(USERNAME_MIN_LENGTH),
            MaxLengthValidator(USERNAME_MAX_LENGTH),
        ],
    )
    first_name = models.CharField(
        _("First name"),
        max_length=FIRST_NAME_MAX_LENGTH,
        blank=True,
    )
    last_name = models.CharField(
        _("Last name"),
        max_length=LAST_NAME_MAX_LENGTH,
        blank=True,
    )
    bio = models.TextField(
        _("Bio"),
        blank=True,
    )
    status = models.CharField(
        _("Status"),
        max_length=STATUS_MAX_LENGTH,
        blank=True,
    )
    photo = ThumbnailerImageField(
        upload_to=UploadAndRenameImage("photos/profiles/"),
        resize_source=dict(
            size=USER_PHOTO_SIZE,
            sharpen=True,
            quality=USER_PHOTO_QUALITY_PERCENT,
        ),
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=USER_PHOTO_ALLOWED_EXTENSIONS,
            )
        ],
        verbose_name=_("Photo"),
    )
    date_joined = models.DateTimeField(
        _("Date joined"),
        default=timezone.now,
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ("username", "is_active")

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self) -> str:
        return f"{self.first_name}"

    def __str__(self) -> str:
        return f"@{self.username}"
