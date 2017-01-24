import django_filters
from housing_backend.models import Affordable
from housing_backend.serializers import AffordableSerializer
from rest_framework import generics

class AffordableFilter(django_filters.rest_framework.FilterSet):
    demographic = django_filters.CharFilter(name="demographic__name")
    housing_size = django_filters.CharFilter(name="housing_size__household_type")

    class Meta:
        model = Affordable
        fields = ['demographic', 'housing_size']


class AffordableList(generics.ListCreateAPIView):
    queryset = Affordable.objects.all()
    serializer_class = AffordableSerializer
    filter_class = AffordableFilter


class AffordableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Affordable.objects.all()
    serializer_class = AffordableSerializer
