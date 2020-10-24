from rest_framework import permissions, viewsets, response

from src.wall.serializers import ListPostSerializer, PostSerializer
from .services import feed_service


class FeedView(viewsets.GenericViewSet):
    """ View follower`s feed
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPostSerializer

    def list(self, request, *args, **kwargs):
        queryset = feed_service.get_post_list(request.user)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = feed_service.get_single_post(kwargs.get('pk'))
        serializer = PostSerializer(instance)
        return response.Response(serializer.data)
