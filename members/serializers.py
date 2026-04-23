import bcrypt
from rest_framework import serializers
from .models import Role, Staff

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    # Optional: If you want to see the role name in the staff response
    role_details = RoleSerializer(source='role', read_only=True)
    
    class Meta:
        model = Staff
        fields = '__all__'
        # Ensure password is write-only for security
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        # Hash the password with bcrypt and salt 10
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10)).decode('utf-8')
        staff = Staff.objects.create(password=hashed_password, **validated_data)
        return staff

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10)).decode('utf-8')
        return super().update(instance, validated_data)
