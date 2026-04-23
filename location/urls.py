from django.urls import path
from .views import CountryViewSet, StateViewSet, DistrictViewSet, TalukViewSet

urlpatterns = [
    # Country URLs
    path('country/list-all', CountryViewSet.as_view({'get': 'list'}), name='country-list-all'),
    path('country/create', CountryViewSet.as_view({'post': 'create'}), name='country-create'),
    path('country/list-by-id/<int:pk>', CountryViewSet.as_view({'get': 'retrieve'}), name='country-list-by-id'),
    path('country/edit/<int:pk>', CountryViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='country-edit'),
    path('country/delete/<int:pk>', CountryViewSet.as_view({'delete': 'destroy'}), name='country-delete'),

    # State URLs
    path('state/list-all', StateViewSet.as_view({'get': 'list'}), name='state-list-all'),
    path('state/create', StateViewSet.as_view({'post': 'create'}), name='state-create'),
    path('state/list-by-id/<int:pk>', StateViewSet.as_view({'get': 'retrieve'}), name='state-list-by-id'),
    path('state/edit/<int:pk>', StateViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='state-edit'),
    path('state/delete/<int:pk>', StateViewSet.as_view({'delete': 'destroy'}), name='state-delete'),

    # District URLs
    path('district/list-all', DistrictViewSet.as_view({'get': 'list'}), name='district-list-all'),
    path('district/create', DistrictViewSet.as_view({'post': 'create'}), name='district-create'),
    path('district/list-by-id/<int:pk>', DistrictViewSet.as_view({'get': 'retrieve'}), name='district-list-by-id'),
    path('district/edit/<int:pk>', DistrictViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='district-edit'),
    path('district/delete/<int:pk>', DistrictViewSet.as_view({'delete': 'destroy'}), name='district-delete'),

    # Taluk URLs
    path('taluk/list-all', TalukViewSet.as_view({'get': 'list'}), name='taluk-list-all'),
    path('taluk/create', TalukViewSet.as_view({'post': 'create'}), name='taluk-create'),
    path('taluk/list-by-id/<int:pk>', TalukViewSet.as_view({'get': 'retrieve'}), name='taluk-list-by-id'),
    path('taluk/edit/<int:pk>', TalukViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='taluk-edit'),
    path('taluk/delete/<int:pk>', TalukViewSet.as_view({'delete': 'destroy'}), name='taluk-delete'),
]
