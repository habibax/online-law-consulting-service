from rest_framework import serializers

from acc.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "created_at",
            "updated_at",
            
        )
        ref_name = "AdminUserSerializer"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "email": instance.email,
            "created_at": instance.created_at,
            "updated_at": instance.updated_at,
            # "first_name": instance.user_profile.first_name if hasattr(instance, "user_profile") else "",
            # "last_name": instance.user_profile.last_name if hasattr(instance, "user_profile") else "",
            # "btc_wallet_address": instance.user_profile.btc_wallet_address if hasattr(instance, "user_profile") else "",
            # "network_wallet_address": instance.user_profile.network_wallet_address if hasattr(instance, "user_profile") else "",
            "is_admin": instance.is_superuser ,
            "is_active":instance.is_active
        }
