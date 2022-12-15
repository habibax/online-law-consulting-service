import logging

from rest_framework import mixins,  viewsets
from rest_framework.permissions import IsAuthenticated

from case.models import Case
from case.serializers import CaseRetrieveSerializer,CaseCreateSerializer

logger=logging.getLogger("basic_logger")

import logging

logger_applog = logging.getLogger("applog")
logger_errors = logging.getLogger("errors")


class CaseViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    permission_classes = (IsAuthenticated,)
    queryset = Case.objects.all()
    serializer_class = CaseRetrieveSerializer
    filter_fields = "__all__"

    def perform_create(self, serializer):
        user = self.request.user
        try:
            serializer.save(user=user)
            message = {
                'message': "case created successfully",
                'user': user.id,
            }
            logger_applog.info(message)
            

        except BaseException as err:
            message = {
                'message': "failed to create case",
                'user': user.id,
                'error': str(err)
            }
            logger_errors.error(message)

    def get_queryset(self):
        user = self.request.user
        return Case.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action == "create":
            return CaseCreateSerializer
        elif self.action in ["retrieve", "list"]:
            return CaseRetrieveSerializer

