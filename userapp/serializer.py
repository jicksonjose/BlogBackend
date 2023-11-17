from rest_framework import serializers
from userapp.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'name',
            'profileimg',
            'email',
            'password'
        )