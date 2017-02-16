from rest_framework import serializers
from housing_backend.models import *


class DemographicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demographic
        exclude = ('id',)


class HousingSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HousingSize
        exclude = ('id',)


class NeighborhoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Neighborhood
        exclude = ('id',)

class AffordableSerializer(serializers.ModelSerializer):
    demographic = DemographicSerializer()
    housing_size = HousingSizeSerializer()
    neighborhood = NeighborhoodSerializer()

    class Meta:
        model = Affordable
        fields = ('affordable', 'demographic', 'housing_size', 'neighborhood')

class RentSerializer(serializers.ModelSerializer):
    housing_size = HousingSizeSerializer()
    nh_id = NeighborhoodSerializer()

    class Meta:
        model = NeighborhoodRent
        fields = ('rent_amt', 'housing_size', 'nh_id')

