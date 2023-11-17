from rest_framework import serializers
from postapp.models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =PostModel
        fields = (
            'userid',
            'title',
            'message'
        )