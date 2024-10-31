from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import apps

app_name = apps.ApiConfig.name

router_v1 = DefaultRouter()

urlpatterns = [
    path("", include(router_v1.urls)),
]
