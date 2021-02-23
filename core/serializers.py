from rest_framework import serializers
from .models import BaiViet


class BaiVietSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaiViet
        fields = (
            'title', 'description', 'owner'
        )
