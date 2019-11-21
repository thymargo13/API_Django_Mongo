from .models import User, Company
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all()
    permission_classes =[
        permissions.AllowAny
    ]
    serializer_class = CompanySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes =[
        permissions.AllowAny
    ]
    serializer_class = UserSerializer 