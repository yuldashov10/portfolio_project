from django.utils.text import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response

from .user import UserViewSet

__all__ = ["ActivateUserAccount"]


class ActivateUserAccount(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        kwargs["data"] = {
            "uid": self.kwargs.get("uid"),
            "token": self.kwargs.get("token"),
        }
        return serializer_class(*args, **kwargs)

    def account_activation(self, request, *args, **kwargs):
        if self.request.user.is_active:
            return Response(
                data={"detail": _("Your account is already active")},
                status=status.HTTP_200_OK,
            )

        super().activation(request, *args, **kwargs)
        return Response(
            data={"detail": _("Your account has been activated")},
            status=status.HTTP_204_NO_CONTENT,
        )
