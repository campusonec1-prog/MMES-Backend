from rest_framework import viewsets
from .models import Country, State, District, Taluk
from .serializers import CountrySerializer, StateSerializer, DistrictSerializer, TalukSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class TenResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('country_name')
    serializer_class = CountrySerializer
    pagination_class = None

class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = State.objects.all().select_related('country').order_by('state_name')
        country_id = self.request.query_params.get('country')
        if country_id:
            queryset = queryset.filter(country_id=country_id)
        return queryset

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    pagination_class = TenResultsSetPagination

    def get_queryset(self):
        queryset = District.objects.all().select_related('state', 'state__country').order_by('district_name')
        
        # Filtering
        district_name = self.request.query_params.get('search')
        state_id = self.request.query_params.get('state')
        country_id = self.request.query_params.get('country')

        if district_name:
            queryset = queryset.filter(district_name__icontains=district_name)
        if state_id:
            queryset = queryset.filter(state_id=state_id)
        if country_id:
            queryset = queryset.filter(state__country_id=country_id)
            
        return queryset

class TalukViewSet(viewsets.ModelViewSet):
    serializer_class = TalukSerializer
    pagination_class = TenResultsSetPagination

    def get_queryset(self):
        queryset = Taluk.objects.all().select_related('district', 'district__state').order_by('taluk_name')
        
        # Filtering
        taluk_name = self.request.query_params.get('search')
        district_id = self.request.query_params.get('district')
        state_id = self.request.query_params.get('state')

        if taluk_name:
            queryset = queryset.filter(taluk_name__icontains=taluk_name)
        if district_id:
            queryset = queryset.filter(district_id=district_id)
        if state_id:
            queryset = queryset.filter(district__state_id=state_id)
            
        return queryset
