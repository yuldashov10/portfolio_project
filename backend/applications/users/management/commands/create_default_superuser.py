from django.core.management.base import BaseCommand
from django.utils.text import gettext_lazy as _

from applications.users.models import User


class Command(BaseCommand):
    help = _("Creates a default superuser if it doesn't exist")

    def handle(self, *args, **options) -> None:
        self.create_default_superuser_for_dev()

    def create_default_superuser_for_dev(self) -> None:
        superuser_data: dict[str, str] = {
            "username": "duck",
            "email": "duck@site.com",
            "password": "1234",
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
            "is_admin": True,
            "is_moder": True,
            "is_vip": True,
            "is_blocked": False,
        }

        username: str = superuser_data.get("username")
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(**superuser_data)
            self.stdout.write(
                self.style.SUCCESS(
                    _(f'Superuser "{username}" created successfully.')
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    _(f'Superuser "{username}" already exists.')
                )
            )
