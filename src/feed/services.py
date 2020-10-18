from src.followers.models import Follower
from src.profiles.models import UserNet
from src.wall.models import Post


def feed(user):
    # NEW

    # Тестов не делал, т.к. не смог развернуть проект на своей машине =(
    # Может быть расскажешь на стриме как развернуть проект?
    # с Django и Python только знакомлюсь... сорян если что=)

    # UPD: Запустил и протестил.

    news = Post.objects.filter(
        user__in=UserNet.objects.filter(owner__subscriber=user)
    ).order_by('-create_date')
    print(news.query)
    print(news)

    # Альтернативный вариант через модель Follow и Values

    news = Post.objects.filter(
        user__in=Follower.objects.values('user').filter(subscriber=user)
    ).order_by('-create_date')
    print(news.query)
    print(news)

    # Вариант с related_name

    news = Post.objects.filter(
        user__owner__subscriber=user
    ).order_by('-create_date')
    print(news.query)
    print(news)
