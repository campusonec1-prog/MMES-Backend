from rest_framework import serializers
from .models import (
    ApplicationMaster, Address, ParentDetails, 
    CoursePreference, AdditionalInfo, UGMarks, PGAcademicRecord,
    StatusMaster, ApplicationStatus, CommunityMaster
)

class CommunityMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityMaster
        fields = '__all__'

class ApplicationMasterSerializer(serializers.ModelSerializer):
    community_name = serializers.CharField(source='community.community_name', read_only=True)
    current_status = serializers.SerializerMethodField()
    course_preferences = serializers.SerializerMethodField()
    pg_academic_records = serializers.SerializerMethodField()
    address_details = serializers.SerializerMethodField()
    parent_details = serializers.SerializerMethodField()
    ug_marks = serializers.SerializerMethodField()
    additional_info = serializers.SerializerMethodField()

    class Meta:
        model = ApplicationMaster
        fields = '__all__'

    def get_current_status(self, obj):
        last_status = ApplicationStatus.objects.filter(application=obj).order_by('-updated_at').first()
        if last_status and last_status.status:
            return last_status.status.status_name
        return "PENDING"

    def get_course_preferences(self, obj):
        prefs = CoursePreference.objects.filter(application=obj).order_by('preference_order')
        return CoursePreferenceSerializer(prefs, many=True).data

    def get_pg_academic_records(self, obj):
        records = PGAcademicRecord.objects.filter(application=obj)
        return PGAcademicRecordSerializer(records, many=True).data

    def get_address_details(self, obj):
        addresses = Address.objects.filter(application=obj)
        return AddressSerializer(addresses, many=True).data

    def get_parent_details(self, obj):
        parent = ParentDetails.objects.filter(application=obj).first()
        return ParentDetailsSerializer(parent).data if parent else None

    def get_ug_marks(self, obj):
        marks = UGMarks.objects.filter(application=obj)
        return UGMarksSerializer(marks, many=True).data

    def get_additional_info(self, obj):
        info = AdditionalInfo.objects.filter(application=obj).first()
        return AdditionalInfoSerializer(info).data if info else None

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ParentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentDetails
        fields = '__all__'

class CoursePreferenceSerializer(serializers.ModelSerializer):
    dept_name = serializers.CharField(source='department.dept_name', read_only=True)
    class Meta:
        model = CoursePreference
        fields = '__all__'

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'

class UGMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UGMarks
        fields = '__all__'

class PGAcademicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGAcademicRecord
        fields = '__all__'

class StatusMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusMaster
        fields = '__all__'

class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = '__all__'
