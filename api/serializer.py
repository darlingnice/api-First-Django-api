from rest_framework import serializers
from core.models import UserData

class UserDataSeializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields ="__all__"
