from django.urls import include, path
from rest_framework import routers

from case.views import CaseViewSet

router = routers.DefaultRouter()
router.register(r"", CaseViewSet, "user-case")


urlpatterns = [
    path("", include(router.urls)),
]
