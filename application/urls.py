from django.urls import path
from .views import (
    ApplicationMasterViewSet, AddressViewSet, ParentDetailsViewSet,
    CoursePreferenceViewSet, AdditionalInfoViewSet, UGMarksViewSet,
    PGAcademicRecordViewSet, StatusMasterViewSet, ApplicationStatusViewSet,
    CommunityMasterViewSet, ApplicantSignupView, ApplicantLoginView, ApplicantProfileView,
    ApplicantUserViewSet
)

urlpatterns = [
    # Application Master URLs
    path('application/list-all', ApplicationMasterViewSet.as_view({'get': 'list'}), name='application-list-all'),
    path('application/create', ApplicationMasterViewSet.as_view({'post': 'create'}), name='application-create'),
    path('application/list-by-id/<int:pk>', ApplicationMasterViewSet.as_view({'get': 'retrieve'}), name='application-list-by-id'),
    path('application/get/<int:pk>', ApplicationMasterViewSet.as_view({'get': 'retrieve'}), name='application-get'),
    path('application/edit/<int:pk>', ApplicationMasterViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='application-edit'),
    path('application/delete/<int:pk>', ApplicationMasterViewSet.as_view({'delete': 'destroy'}), name='application-delete'),

    # Address URLs
    path('address/list-all', AddressViewSet.as_view({'get': 'list'}), name='address-list-all'),
    path('address/create', AddressViewSet.as_view({'post': 'create'}), name='address-create'),
    path('address/list-by-id/<int:pk>', AddressViewSet.as_view({'get': 'retrieve'}), name='address-list-by-id'),
    path('address/edit/<int:pk>', AddressViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='address-edit'),
    path('address/delete/<int:pk>', AddressViewSet.as_view({'delete': 'destroy'}), name='address-delete'),

    # Parent Details URLs
    path('parent-details/list-all', ParentDetailsViewSet.as_view({'get': 'list'}), name='parent-details-list-all'),
    path('parent-details/create', ParentDetailsViewSet.as_view({'post': 'create'}), name='parent-details-create'),
    path('parent-details/list-by-id/<int:pk>', ParentDetailsViewSet.as_view({'get': 'retrieve'}), name='parent-details-list-by-id'),
    path('parent-details/edit/<int:pk>', ParentDetailsViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='parent-details-edit'),
    path('parent-details/delete/<int:pk>', ParentDetailsViewSet.as_view({'delete': 'destroy'}), name='parent-details-delete'),

    # Course Preference URLs
    path('course-preference/list-all', CoursePreferenceViewSet.as_view({'get': 'list'}), name='course-preference-list-all'),
    path('course-preference/create', CoursePreferenceViewSet.as_view({'post': 'create'}), name='course-preference-create'),
    path('course-preference/list-by-id/<int:pk>', CoursePreferenceViewSet.as_view({'get': 'retrieve'}), name='course-preference-list-by-id'),
    path('course-preference/edit/<int:pk>', CoursePreferenceViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='course-preference-edit'),
    path('course-preference/delete/<int:pk>', CoursePreferenceViewSet.as_view({'delete': 'destroy'}), name='course-preference-delete'),

    # Additional Info URLs
    path('additional-info/list-all', AdditionalInfoViewSet.as_view({'get': 'list'}), name='additional-info-list-all'),
    path('additional-info/create', AdditionalInfoViewSet.as_view({'post': 'create'}), name='additional-info-create'),
    path('additional-info/list-by-id/<int:pk>', AdditionalInfoViewSet.as_view({'get': 'retrieve'}), name='additional-info-list-by-id'),
    path('additional-info/edit/<int:pk>', AdditionalInfoViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='additional-info-edit'),
    path('additional-info/delete/<int:pk>', AdditionalInfoViewSet.as_view({'delete': 'destroy'}), name='additional-info-delete'),

    # UG Marks URLs
    path('ug-marks/list-all', UGMarksViewSet.as_view({'get': 'list'}), name='ug-marks-list-all'),
    path('ug-marks/create', UGMarksViewSet.as_view({'post': 'create'}), name='ug-marks-create'),
    path('ug-marks/list-by-id/<int:pk>', UGMarksViewSet.as_view({'get': 'retrieve'}), name='ug-marks-list-by-id'),
    path('ug-marks/edit/<int:pk>', UGMarksViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='ug-marks-edit'),
    path('ug-marks/delete/<int:pk>', UGMarksViewSet.as_view({'delete': 'destroy'}), name='ug-marks-delete'),

    # PG Academic Record URLs
    path('pg-record/list-all', PGAcademicRecordViewSet.as_view({'get': 'list'}), name='pg-record-list-all'),
    path('pg-record/create', PGAcademicRecordViewSet.as_view({'post': 'create'}), name='pg-record-create'),
    path('pg-record/list-by-id/<int:pk>', PGAcademicRecordViewSet.as_view({'get': 'retrieve'}), name='pg-record-list-by-id'),
    path('pg-record/edit/<int:pk>', PGAcademicRecordViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='pg-record-edit'),
    path('pg-record/delete/<int:pk>', PGAcademicRecordViewSet.as_view({'delete': 'destroy'}), name='pg-record-delete'),

    # Status Master URLs
    path('status-master/list-all', StatusMasterViewSet.as_view({'get': 'list'}), name='status-master-list-all'),
    path('status-master/create', StatusMasterViewSet.as_view({'post': 'create'}), name='status-master-create'),
    path('status-master/list-by-id/<int:pk>', StatusMasterViewSet.as_view({'get': 'retrieve'}), name='status-master-list-by-id'),
    path('status-master/edit/<int:pk>', StatusMasterViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='status-master-edit'),
    path('status-master/delete/<int:pk>', StatusMasterViewSet.as_view({'delete': 'destroy'}), name='status-master-delete'),

    # Application Status URLs
    path('application-status/list-all', ApplicationStatusViewSet.as_view({'get': 'list'}), name='application-status-list-all'),
    path('application-status/create', ApplicationStatusViewSet.as_view({'post': 'create'}), name='application-status-create'),
    path('application-status/list-by-id/<int:pk>', ApplicationStatusViewSet.as_view({'get': 'retrieve'}), name='application-status-list-by-id'),
    path('application-status/edit/<int:pk>', ApplicationStatusViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='application-status-edit'),
    path('application-status/delete/<int:pk>', ApplicationStatusViewSet.as_view({'delete': 'destroy'}), name='application-status-delete'),

    # Community Master URLs
    path('community-master/list-all', CommunityMasterViewSet.as_view({'get': 'list'}), name='community-master-list-all'),
    path('community-master/create', CommunityMasterViewSet.as_view({'post': 'create'}), name='community-master-create'),
    path('community-master/list-by-id/<int:pk>', CommunityMasterViewSet.as_view({'get': 'retrieve'}), name='community-master-list-by-id'),
    path('community-master/edit/<int:pk>', CommunityMasterViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='community-master-edit'),
    path('community-master/delete/<int:pk>', CommunityMasterViewSet.as_view({'delete': 'destroy'}), name='community-master-delete'),

    # Applicant User Admin URLs
    path('applicant-users/list-all', ApplicantUserViewSet.as_view({'get': 'list'}), name='applicant-user-list-all'),
    path('applicant-users/create', ApplicantUserViewSet.as_view({'post': 'create'}), name='applicant-user-create'),
    path('applicant-users/list-by-id/<int:pk>', ApplicantUserViewSet.as_view({'get': 'retrieve'}), name='applicant-user-list-by-id'),
    path('applicant-users/edit/<int:pk>', ApplicantUserViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='applicant-user-edit'),
    path('applicant-users/delete/<int:pk>', ApplicantUserViewSet.as_view({'delete': 'destroy'}), name='applicant-user-delete'),

    # Applicant Auth URLs
    path('auth/signup', ApplicantSignupView.as_view(), name='applicant-signup'),
    path('auth/login', ApplicantLoginView.as_view(), name='applicant-login'),
    path('auth/profile/', ApplicantProfileView.as_view(), name='applicant-profile'),
]

