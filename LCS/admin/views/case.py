from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework import mixins, response, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from admin.serializers import AdminCaseRetrieveSerializer
from common.permission import IsAdmin
from case.models import Case


class CaseViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = AdminCaseRetrieveSerializer
    queryset = Case.objects.all()
    search_fields = ("user_email",)
    filter_fields = "__all__"
    ordering = ("-created_at",)

    @swagger_auto_schema(
        method="post",
        request_body=no_body,
        operation_description="Accept case",
        responses={
            status.HTTP_202_ACCEPTED: "OK",
            status.HTTP_404_NOT_FOUND: "case not found.",
            status.HTTP_400_BAD_REQUEST: "Invalid case.",
        },
    )
    @action(detail=True, methods=["post"])
    def accept(self, request, pk):
        instance = self.get_object()

        if instance.state != Case.State.PENDING_ADMIN:
            return response.Response(
                {"detail": "Invalid case!"}, status=status.HTTP_400_BAD_REQUEST
            )

        instance.state = Case.State.PENDING_LAWYER
        instance.save()

        return response.Response(
            {"detail": "case accepted by admin!"}, status=status.HTTP_202_ACCEPTED
        )

    @swagger_auto_schema(
        method="post",
        request_body=no_body,
        operation_description="Reject Case",
        responses={
            status.HTTP_204_NO_CONTENT: "OK",
            status.HTTP_404_NOT_FOUND: "case not found.",
            status.HTTP_400_BAD_REQUEST: "Invalid case.",
        },
    )
    @action(detail=True, methods=["post"])
    def reject(self, request, pk):
        instance = self.get_object()

        if instance.state != Case.State.PENDING_ADMIN:
            return response.Response(
                {"detail": "Invalid case!"}, status=status.HTTP_400_BAD_REQUEST
            )

        instance.state = Case.State.REJECTED
        instance.save()

        return response.Response(
            {"detail": "Case rejected!"}, status=status.HTTP_204_NO_CONTENT
        )
