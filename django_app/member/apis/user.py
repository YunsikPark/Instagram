from rest_framework import permissions, generics

from member.serializers import UserSerializer, UserCreationSerializer
from utils.permissions import ObjectIsRequestUser
from ..models import User

__all__ = (
    'UserRetrieveUpdateDestroyView',
    'UserListCreateView',
)


# UserListCreateView
# generics.ListCreateAPIView사용
# 완료 후 두 APIView를 Postman에 등록 후 테스트
#   List, Create, Retrieve, Update, Destroy 전부

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        elif self.request.method == 'POST':
            return UserCreationSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ObjectIsRequestUser,
    )

