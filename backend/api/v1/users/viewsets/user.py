from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet as DjoerUserViewSet
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.users.serializers import UserSerializer, UserShortInfoSerializer
from applications.users.models import User

__all__ = ["UserViewSet"]


class UserViewSet(DjoerUserViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ("is_active", "is_vip", "is_blocked")
    search_fields = ("username", "email")
    lookup_field = "id"
    http_method_names = ["patch", "get", "post", "delete"]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self) -> User:
        return User.objects.get_user_by_public_id(self.kwargs.get("id"))

    def get_serializer_class(self):
        if self.action == "list":
            return UserShortInfoSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "me":
            return (IsAuthenticated(),)
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        get_object_or_404(
            User,
            public_id=self.kwargs.get("id"),
        ).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
