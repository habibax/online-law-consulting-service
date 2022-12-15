from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework import mixins, response, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from acc.models import User
from admin.serializers import UserSerializer
from common.permission import IsAdmin


class UserViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated, IsAdmin)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]
    ordering_fields = ("created_at",)
    ordering = ("-created_at",)

    @swagger_auto_schema(
        method="post",
        request_body=no_body,
        responses={
            status.HTTP_202_ACCEPTED: "User activated",
            status.HTTP_404_NOT_FOUND: "User not found",
        },
    )
    @action(detail=True, methods=["post"])
    def activate(self, request, pk):
        instance = self.get_object()

        instance.is_active = True
        instance.save()

        return response.Response(
            {"detail": "User activated"}, status=status.HTTP_204_NO_CONTENT
        )
