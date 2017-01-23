from rest_framework import serializers
from housing_backend.models import Affordable


class AffordableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affordable
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')