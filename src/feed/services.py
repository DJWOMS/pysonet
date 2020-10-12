from django.conf import settings
from django.contrib.auth.models import User
from src.followers.models import Follower
from src.profiles.models import UserNet
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

    # NEW
    # Прямая связь между моделями Follower и Post отсутствует
    # связь организеум через модель User.
    # Возможно User надо поменять на твою модель UserNet или settings.AUTH_USER_MODEL
    # Ниже все 3 варианта =)
    # Тестов не делал, т.к. не смог развернуть проект на своей машине =(
    # Может быть расскажешь на стриме как развернуть данный проект?
    # с Django и Python только знакомлюсь... сорян если что=)

    # 1 User
    news = Post.objects.filter(
        user__in=User.objects.filter(owner__subscriber=user),
        create_date__hour=1
    ).order_by('-create_date')
    print(news.count())

    # 2 UserNet
    news = Post.objects.filter(
        user__in=UserNet.objects.filter(owner__subscriber=user),
        create_date__hour=1
    ).order_by('-create_date')
    print(news.count())

    # 2 settings.AUTH_USER_MODEL
    news = Post.objects.filter(
        user__in=settings.AUTH_USER_MODEL.objects.filter(owner__subscriber=user),
        create_date__hour=1
    ).order_by('-create_date')
    print(news.count())
