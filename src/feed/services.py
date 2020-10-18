from src.followers.models import Follower
from src.wall.models import Post


def feed(user):
    # 1
    posts = Post.objects.filter(user__owner__subscriber_id=1).order_by('-create_date')\
        .select_related('user').prefetch_related('comments')
