from django.urls import path
from .views import DepartmentViewSet

urlpatterns = [
    # Department URLs
    path('department/list-all', DepartmentViewSet.as_view({'get': 'list'}), name='department-list-all'),
    path('department/create', DepartmentViewSet.as_view({'post': 'create'}), name='department-create'),
    path('department/list-by-id/<int:pk>', DepartmentViewSet.as_view({'get': 'retrieve'}), name='department-list-by-id'),
    path('department/edit/<int:pk>', DepartmentViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='department-edit'),
    path('department/delete/<int:pk>', DepartmentViewSet.as_view({'delete': 'destroy'}), name='department-delete'),
]
