from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import jwt
import datetime
from .models import (
    ApplicationMaster, Address, ParentDetails, 
    CoursePreference, AdditionalInfo, UGMarks, PGAcademicRecord,
    StatusMaster, ApplicationStatus, CommunityMaster, ApplicantUser
)
from .serializers import (
    ApplicationMasterSerializer, AddressSerializer, ParentDetailsSerializer,
    CoursePreferenceSerializer, AdditionalInfoSerializer, UGMarksSerializer,
    PGAcademicRecordSerializer, StatusMasterSerializer, ApplicationStatusSerializer,
    CommunityMasterSerializer, ApplicantUserSerializer
)

class CommunityMasterViewSet(viewsets.ModelViewSet):
    queryset = CommunityMaster.objects.all()
    serializer_class = CommunityMasterSerializer

class ApplicationMasterViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationMasterSerializer

    def get_queryset(self):
        queryset = ApplicationMaster.objects.all().order_by('-created_at')
        user_id = self.request.query_params.get('applicant_user_id')
        if user_id:
            queryset = queryset.filter(applicant_user_id=user_id)
        return queryset

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

class ApplicantUserViewSet(viewsets.ModelViewSet):
    queryset = ApplicantUser.objects.all().order_by('-created_at')
    serializer_class = ApplicantUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if 'password' in self.request.data and self.request.data['password']:
            user.set_password(self.request.data['password'])
            user.save()

    def perform_update(self, serializer):
        user = serializer.save()
        if 'password' in self.request.data and self.request.data['password']:
            user.set_password(self.request.data['password'])
            user.save()

class ApplicantSignupView(APIView):
    def post(self, request):
        full_name = request.data.get('full_name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')

        if not full_name or not email or not password:
            return Response({'error': 'All required fields must be provided'}, status=status.HTTP_400_BAD_REQUEST)

        if ApplicantUser.objects.filter(email=email).exists():
            return Response({'error': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = ApplicantUser(full_name=full_name, email=email, phone=phone)
        user.set_password(password)
        user.save()

        return Response({
            'message': 'User registered successfully',
            'user': {
                'id': user.user_id,
                'full_name': user.full_name,
                'email': user.email,
                'phone': user.phone
            }
        }, status=status.HTTP_201_CREATED)

class ApplicantLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = ApplicantUser.objects.get(email=email)
        except ApplicantUser.DoesNotExist:
            return Response({'error': 'Invalid email credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'error': 'Invalid password credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            'user_id': user.user_id,
            'email': user.email,
            'full_name': user.full_name,
            'role': 'applicant',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return Response({
            'message': 'Login successful',
            'token': token,
            'user': {
                'id': user.user_id,
                'full_name': user.full_name,
                'email': user.email,
                'phone': user.phone
            }
        }, status=status.HTTP_200_OK)

class ApplicantProfileView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error': 'No token provided'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = ApplicantUser.objects.get(user_id=payload['user_id'])
            return Response({
                'user_id': user.user_id,
                'full_name': user.full_name,
                'email': user.email,
                'phone': user.phone
            })
        except Exception as e:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_401_UNAUTHORIZED)
