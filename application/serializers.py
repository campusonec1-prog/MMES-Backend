from rest_framework import serializers
from .models import (
    ApplicationMaster, Address, ParentDetails, 
    CoursePreference, AdditionalInfo, UGMarks, PGAcademicRecord,
    StatusMaster, ApplicationStatus, CommunityMaster, ApplicantUser
)
from location.models import Country, State, District, Taluk

class CommunityMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityMaster
        fields = '__all__'

class ApplicationMasterSerializer(serializers.ModelSerializer):
    community_name = serializers.CharField(source='community.community_name', read_only=True)
    current_status = serializers.CharField(required=False)
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
        last_status = obj.status_history.order_by('-app_status_id').first()
        if last_status and last_status.status:
            return last_status.status.status_name
        return "PENDING"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['current_status'] = self.get_current_status(instance)
        return ret

    def update(self, instance, validated_data):
        status_name = validated_data.pop('current_status', None)
        
        # Update Master fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle Status Update
        if status_name:
            from .models import StatusMaster, ApplicationStatus
            status_obj, _ = StatusMaster.objects.get_or_create(status_name=status_name.upper())
            ApplicationStatus.objects.create(
                application=instance,
                status=status_obj,
                remarks=f"Status updated to {status_name}"
            )
        
        return instance

    def get_course_preferences(self, obj):
        return CoursePreferenceSerializer(obj.course_preferences.all().order_by('preference_order'), many=True).data

    def get_pg_academic_records(self, obj):
        return PGAcademicRecordSerializer(obj.pg_records.all(), many=True).data

    def get_address_details(self, obj):
        return AddressSerializer(obj.addresses.all(), many=True).data

    def get_parent_details(self, obj):
        parent = obj.parent_details.first()
        return ParentDetailsSerializer(parent).data if parent else None

    def get_ug_marks(self, obj):
        return UGMarksSerializer(obj.ug_marks.all(), many=True).data

    def get_additional_info(self, obj):
        info = obj.additional_info.first()
        return AdditionalInfoSerializer(info).data if info else None

class AddressSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), required=False, allow_null=True)
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all(), required=False, allow_null=True)
    district = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), required=False, allow_null=True)
    taluk = serializers.PrimaryKeyRelatedField(queryset=Taluk.objects.all(), required=False, allow_null=True)
    
    country_name = serializers.CharField(source='country.country_name', read_only=True)
    state_name = serializers.CharField(source='state.state_name', read_only=True)
    district_name = serializers.CharField(source='district.district_name', read_only=True)
    taluk_name = serializers.CharField(source='taluk.taluk_name', read_only=True)

    class Meta:
        model = Address
        fields = [
            'address_id', 'application', 'address_type', 'address',
            'country', 'state', 'district', 'taluk', 'pincode',
            'country_name', 'state_name', 'district_name', 'taluk_name',
            'other_district', 'other_taluk'
        ]

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

class ApplicantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantUser
        fields = ['user_id', 'full_name', 'email', 'phone', 'password', 'created_at']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}
