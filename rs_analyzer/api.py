from rs_analyzer.models import Users
from rest_framework import viewsets, permissions
from rs_analyzer.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
