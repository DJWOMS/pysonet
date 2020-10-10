from src.followers.models import Follower
from src.wall.models import Post


def feed(user):
    # 1
    news = []
    subscribe = Follower.objects.filter(subscriber=user).values()
    for sub in subscribe:
        news.append(Post.objects.filter(user=sub.user, create_date__hour=1).order_by('-create_date'))

    # 2
    Post.objects.filter(user__id__in=subscribe, create_date__hour=1).order_by('-create_date')
    user.post.fiter(user__in=subscribe)
