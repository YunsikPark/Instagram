from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Post
from ..serializers.post import PostSerializer

__all__ = (
    'PostListView',
)


class PostListView(APIView):
    # get요청이 왔을 때, Post.objects.all()을
    # PostSerializer를 통해 Response로 반환
    # DRF API Guide
    #   - API View
    #   - Serializers
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
