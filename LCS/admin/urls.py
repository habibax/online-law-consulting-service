from django.urls import include, path
from rest_framework import routers

from admin.views import (
    CaseViewSet,
)

router = routers.DefaultRouter()
router.register(r"case", CaseViewSet, "admin-case")


urlpatterns = [
    path("", include(router.urls)),
]
