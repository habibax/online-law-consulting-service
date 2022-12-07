from django.urls import include, path
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from acc.views import AdminProfileViewSet, CustomDjoserViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r"profile", UserProfileViewSet, "profile")
router.register(r"admin-profile", AdminProfileViewSet, "admin-profile")
router.register(r"auth", CustomDjoserViewSet, "djoser-auth")

urlpatterns = [
    path(r"", include(router.urls)),
    # path(r"auth/", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.authtoken")),
    path("django-admin", admin.site.urls),
    path("account/", include("acc.urls")),
]
urlpatterns += staticfiles_urlpatterns()