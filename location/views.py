from rest_framework import viewsets
from .models import Country, State, District, Taluk
from .serializers import CountrySerializer, StateSerializer, DistrictSerializer, TalukSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    pagination_class = None

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    pagination_class = None

class TalukViewSet(viewsets.ModelViewSet):
    queryset = Taluk.objects.all()
    serializer_class = TalukSerializer
    pagination_class = None
