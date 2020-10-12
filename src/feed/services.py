from src.profiles.models import UserNet
from src.wall.models import Post


def feed(user):
    # NEW
    # Прямая связь между моделями Follower и Post отсутствует
    # связь организеум через модель User.
    # Возможно User надо поменять на твою модель UserNet или settings.AUTH_USER_MODEL
    # Ниже все 3 варианта =)
    # Тестов не делал, т.к. не смог развернуть проект на своей машине =(
    # Может быть расскажешь на стриме как развернуть данный проект?
    # с Django и Python только знакомлюсь... сорян если что=)

    # UPD: Запустил и протестил.

    news = Post.objects.filter(
        user__in=UserNet.objects.filter(owner__subscriber=user)
    ).order_by('-create_date')
    print(news.count())
    print(news)
