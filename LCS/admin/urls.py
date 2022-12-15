from django.urls import include, path
from rest_framework import routers

from admin.views import (
    CaseViewSet,
    UserViewSet,
)

router = routers.DefaultRouter()
router.register(r"case", CaseViewSet, "admin-case")
router.register(r"user", UserViewSet, "user")




urlpatterns = [
    path("", include(router.urls)),
]
