from django.urls import path
from .views import RoleViewSet, StaffViewSet, LoginView

urlpatterns = [
    # Auth
    path('staff/login', LoginView.as_view(), name='login'),

    # Role URLs
    path('role/list-all', RoleViewSet.as_view({'get': 'list'}), name='role-list-all'),
    path('role/create', RoleViewSet.as_view({'post': 'create'}), name='role-create'),
    path('role/list-by-id/<int:pk>', RoleViewSet.as_view({'get': 'retrieve'}), name='role-list-by-id'),
    path('role/edit/<int:pk>', RoleViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='role-edit'),
    path('role/delete/<int:pk>', RoleViewSet.as_view({'delete': 'destroy'}), name='role-delete'),

    # Staff URLs
    path('staff/list-all', StaffViewSet.as_view({'get': 'list'}), name='staff-list-all'),
    path('staff/create', StaffViewSet.as_view({'post': 'create'}), name='staff-create'),
    path('staff/list-by-id/<int:pk>', StaffViewSet.as_view({'get': 'retrieve'}), name='staff-list-by-id'),
    path('staff/edit/<int:pk>', StaffViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='staff-edit'),
    path('staff/delete/<int:pk>', StaffViewSet.as_view({'delete': 'destroy'}), name='staff-delete'),
]
