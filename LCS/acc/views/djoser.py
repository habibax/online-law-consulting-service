from genericpath import exists
from django.utils.timezone import now
from djoser import signals
from djoser.conf import settings
from djoser.views import UserViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from acc.models import User




class CustomDjoserViewSet(UserViewSet):
    permission_classes = (IsAuthenticated,)
    lookup_field = None

    def get_object(self):
        return self.request.user

    def set_username(self, request, *args, **kwargs):
        raise NotImplementedError

    def reset_username(self, request, *args, **kwargs):
        raise NotImplementedError

    def reset_username_confirm(self, request, *args, **kwargs):
        raise NotImplementedError

    def set_password(self, request, *args, **kwargs):
        raise NotImplementedError

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        raise NotImplementedError

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        raise NotImplementedError

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        raise NotImplementedError

    @swagger_auto_schema(auto_schema=None)
    def list(self, request, *args, **kwargs):
        raise NotImplementedError

    @action(["get"], detail=False)
    def me(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @action(["get"], detail=False)
    def permissions(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(
            {"stake": instance.groups.filter(name="stake").exists()},
            status=status.HTTP_200_OK,
        )

    def perform_create(self, serializer):
        user = serializer.save()
        user_object=User.objects.get(email=user.email)
        user_object.set_password(user.password)
        user_object.save()
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )



    @action(["post"], detail=False)
    def activation(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user.is_active = True
        user.save()

        signals.user_activated.send(
            sender=self.__class__, user=user, request=self.request
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["post"], detail=False)
    def resend_activation(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get_user(is_active=False)

        if not settings.SEND_ACTIVATION_EMAIL or not user:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get_user()
        user_email=serializer.validated_data.get("email")
        
        user_object=User.objects.filter(email=user_email).exists()
        if user:
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif user_object:
            return Response(status=status.HTTP_401_UNAUTHORIZED)            
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
            

        

    @action(["post"], detail=False)
    def reset_password_confirm(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.user.set_password(serializer.data["new_password"])
        if hasattr(serializer.user, "last_login"):
            serializer.user.last_login = now()
        serializer.user.save()



        return Response(status=status.HTTP_204_NO_CONTENT)
