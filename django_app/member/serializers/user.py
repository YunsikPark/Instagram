from rest_framework import serializers

from ..models import User

__all__ = (
    'UserSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
        )


# serializers 의 __init__ 파일 구현
# urls 에 urls_apis, urls_views 로 파일 구분
# apis 에 user.py 모듈 생성, UserRetrieveUpdateDestroyView 구현
#   urls.urls_apis 에 UserRetrieveUpdateDestroyView.as_view()를 연결

# config.urls.urls_apis에 member.urls.urls_apis 를 연결
