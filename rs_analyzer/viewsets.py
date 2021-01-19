from rs_analyzer.models import Users, Support
from rest_framework import viewsets, permissions
from rs_analyzer.serializers import UserSerializer, SupportSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class SupportViewSet(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SupportSerializer
    default_response_headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Headers": "*"
    }
