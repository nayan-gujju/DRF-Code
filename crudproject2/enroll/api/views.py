from rest_framework.viewsets import ModelViewSet
from enroll.models import User
from enroll.api.serializers import UserSerializer

class UserApi(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 