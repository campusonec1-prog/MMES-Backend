from rest_framework import viewsets
from .models import (
    ApplicationMaster, Address, ParentDetails, 
    CoursePreference, AdditionalInfo, UGMarks, PGAcademicRecord,
    StatusMaster, ApplicationStatus, CommunityMaster
)
from .serializers import (
    ApplicationMasterSerializer, AddressSerializer, ParentDetailsSerializer,
    CoursePreferenceSerializer, AdditionalInfoSerializer, UGMarksSerializer,
    PGAcademicRecordSerializer, StatusMasterSerializer, ApplicationStatusSerializer,
    CommunityMasterSerializer
)

class CommunityMasterViewSet(viewsets.ModelViewSet):
    queryset = CommunityMaster.objects.all()
    serializer_class = CommunityMasterSerializer

class ApplicationMasterViewSet(viewsets.ModelViewSet):
    queryset = ApplicationMaster.objects.all()
    serializer_class = ApplicationMasterSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ParentDetailsViewSet(viewsets.ModelViewSet):
    queryset = ParentDetails.objects.all()
    serializer_class = ParentDetailsSerializer

class CoursePreferenceViewSet(viewsets.ModelViewSet):
    queryset = CoursePreference.objects.all()
    serializer_class = CoursePreferenceSerializer

class AdditionalInfoViewSet(viewsets.ModelViewSet):
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoSerializer

class UGMarksViewSet(viewsets.ModelViewSet):
    queryset = UGMarks.objects.all()
    serializer_class = UGMarksSerializer

class PGAcademicRecordViewSet(viewsets.ModelViewSet):
    queryset = PGAcademicRecord.objects.all()
    serializer_class = PGAcademicRecordSerializer

class StatusMasterViewSet(viewsets.ModelViewSet):
    queryset = StatusMaster.objects.all()
    serializer_class = StatusMasterSerializer

class ApplicationStatusViewSet(viewsets.ModelViewSet):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer
