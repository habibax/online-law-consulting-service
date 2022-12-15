from django.urls import include, path
from rest_framework import routers

from lawyer.views import (
    CaseViewSet,
)

router = routers.DefaultRouter()
router.register(r"case", CaseViewSet, "lawyer-case")


urlpatterns = [
    path("", include(router.urls)),
]
