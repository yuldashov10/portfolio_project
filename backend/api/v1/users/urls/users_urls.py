from django.urls import path

from api.v1.users.viewsets import UserViewSet

users_patterns = [
    path(
        "me/",
        UserViewSet.as_view({"get": "me"}),
        name="me_detail",
    ),
    path(
        "me/edit/",
        UserViewSet.as_view({"patch": "me"}),
        name="me_edit",
    ),
    path(
        "",
        UserViewSet.as_view({"get": "list"}),
        name="users_list",
    ),
    path(
        "<str:id>/",
        UserViewSet.as_view({"get": "retrieve"}),
        name="user_detail",
    ),
    path(
        "<str:id>/edit/",
        UserViewSet.as_view({"patch": "partial_update"}),
        name="user_edit",
    ),
    path(
        "<str:id>/delete/",
        UserViewSet.as_view({"delete": "destroy"}),
        name="user_delete",
    ),
]
