from django.urls import include, path
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from acc.views import  CustomDjoserViewSet

router = routers.DefaultRouter()
router.register(r"auth", CustomDjoserViewSet, "djoser-auth")

urlpatterns = [
    path(r"", include(router.urls)),
    # path(r"auth/", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.authtoken")),

]
urlpatterns += staticfiles_urlpatterns()