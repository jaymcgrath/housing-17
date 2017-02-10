import django_filters
from housing_backend.models import Affordable, NeighborhoodRent
from housing_backend.serializers import AffordableSerializer, RentSerializer
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

class RentFilter(django_filters.rest_framework.FilterSet):
    rent_amt = django_filters.NumberFilter(name="rent_amt", lookup_expr="rent")
    rent_amt_gt = django_filters.NumberFilter(name="rent_amt", lookup_expr="gt")
    rent_amt_lt = django_filters.NumberFilter(name="rent_amt", lookup_expr="lt")
    housing_size = django_filters.CharFilter(name="housing_size__household_type")

    class Meta:
        model = NeighborhoodRent
        fields = ['rent_amt', 'housing_size']

class RentList(generics.ListCreateAPIView):
    queryset = NeighborhoodRent.objects.all()
    serializer_class = RentSerializer
    filter_class = RentFilter

class RentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NeighborhoodRent.objects.all()
    serializer_class = RentSerializer


