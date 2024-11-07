from django.db import models
from django.utils.text import gettext_lazy as _

__all__ = ["UserStatusMixin"]


class UserStatusMixin(models.Model):
    """
    Mixin that adds user status fields to a model.

    This mixin provides the following boolean fields to the model:

    - `is_staff`: Indicates whether the user is a staff member.
    - `is_superuser`: Indicates whether the user has superuser privileges.
    - `is_active`: Indicates whether the user account is active.
    - `is_admin`: Indicates whether the user is an administrator.
    - `is_moder`: Indicates whether the user is a moderator.
    - `is_vip`: Indicates whether the user is a VIP.
    - `is_blocked`: Indicates whether the user is blocked.

    This mixin is intended to be used as an abstract base
    class and is not meant to be instantiated directly.
    """

    is_staff = models.BooleanField(
        _("Staff status"),
        default=False,
        help_text=_(
            "Indicates whether the user can log into the admin panel."
        ),
    )
    is_superuser = models.BooleanField(
        _("Superuser status"),
        default=False,
        help_text=_(
            "Indicates that this user has all permissions "
            "without explicitly assigning them."
        ),
    )
    is_active = models.BooleanField(
        _("Active"),
        default=False,
        help_text=_(
            "Indicates whether this user should be considered active. "
            "Clear this check box instead of deleting accounts."
        ),
    )
    is_admin = models.BooleanField(
        _("Admin status"),
        default=False,
        help_text=_("Indicates whether the user has admin rights."),
    )
    is_moder = models.BooleanField(
        _("Moderator status"),
        default=False,
        help_text=_("Indicates whether the user has moderator rights."),
    )
    is_vip = models.BooleanField(
        _("VIP status"),
        default=False,
        help_text=_("Indicates whether the user is a VIP member."),
    )
    is_blocked = models.BooleanField(
        _("Blocked"),
        default=False,
        help_text=_(
            "Indicates whether the user is blocked "
            "and cannot access the platform."
        ),
    )

    class Meta:
        abstract = True
