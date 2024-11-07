from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.text import gettext_lazy as _

from applications.users.constants import USERS_PER_PAGE
from applications.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "is_active")
    list_display_links = ("username",)
    list_filter = ("is_active",)
    list_per_page = USERS_PER_PAGE
    search_fields = ("username", "email", "id")
    readonly_fields = ("id",)
    fieldsets = (
        (
            _("Main information"),
            {
                "fields": ("id", "username", "email"),
                "classes": ("wide",),
                "description": _(
                    "This is the user model where you can change "
                    "user information or add a new user."
                ),
            },
        ),
        (
            _("Status"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "is_admin",
                    "is_moder",
                    "is_vip",
                    "is_blocked",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            _("Additional Information"),
            {
                "fields": (
                    "photo",
                    "status",
                    "bio",
                    "first_name",
                    "last_name",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Date information",
            {
                "fields": ("date_joined", "last_login"),
                "classes": ("collapse",),
            },
        ),
    )


admin.site.empty_value_display = _("Not specified")
