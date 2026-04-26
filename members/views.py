import jwt
import datetime
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Role, Staff
from .serializers import RoleSerializer, StaffSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class = None

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 1. Validate input
        if not username or not password:
            return Response({
                'error': 'Username and password are required',
                'message': 'Please provide both username and password'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 2. Find the staff member
            staff = Staff.objects.get(username=username)
        except Staff.DoesNotExist:
            return Response({
                'error': 'Invalid username',
                'message': f'No staff member found with username: {username}'
            }, status=status.HTTP_401_UNAUTHORIZED)

        # 3. Check password
        if not staff.check_password(password):
            return Response({
                'error': 'Invalid password',
                'message': 'The password you entered is incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)

        # 4. Generate JWT
        payload = {
            'staff_id': staff.id,
            'username': staff.username,
            'role': staff.role.role_name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return Response({
            'message': 'Login successful',
            'token': token,
            'staff': {
                'id': staff.id,
                'first_name': staff.first_name,
                'last_name': staff.last_name,
                'username': staff.username,
                'role': staff.role.role_name
            }
        }, status=status.HTTP_200_OK)
