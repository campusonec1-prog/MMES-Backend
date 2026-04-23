from rest_framework import viewsets
from .models import Country, State, District, Taluk
from .serializers import CountrySerializer, StateSerializer, DistrictSerializer, TalukSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class TalukViewSet(viewsets.ModelViewSet):
    queryset = Taluk.objects.all()
    serializer_class = TalukSerializer
