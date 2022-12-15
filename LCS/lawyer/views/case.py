from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework import mixins, response, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from lawyer.serializers import LawyerCaseRetrieveSerializer
from case.models import Case
from acc.models import User


class CaseViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
):
    permission_classes = (IsAuthenticated,)
    serializer_class = LawyerCaseRetrieveSerializer
    queryset = Case.objects.filter(state="pending_lawyer")
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

        if instance.state != Case.State.PENDING_LAWYER:
            return response.Response(
                {"detail": "Invalid case!"}, status=status.HTTP_400_BAD_REQUEST
            )

        instance.state = Case.State.ACCEPTED
        instance.lawyer=User.objects.get(pk=self.request.user.id)
        instance.save()

        return response.Response(
            {"detail": "case accepted by you here is clients contact!",
             "client contact":User.objects.get(pk=instance.user.id).email}, status=status.HTTP_202_ACCEPTED
        )
