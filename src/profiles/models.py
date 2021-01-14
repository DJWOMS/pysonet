import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class UserNet(AbstractUser):
    """ Custom user model
    """
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    technology = models.ManyToManyField('Technology', related_name='users')


@receiver(pre_save, sender=UserNet)
def post_update(sender, instance, **kwargs):
    """
    Удаление старого аватара после обновления
    """
    if not instance.pk:
        return False

    if sender.objects.get(pk=instance.pk).avatar:
        old_avatar = sender.objects.get(pk=instance.pk).avatar
        new_avatar = instance.avatar
        if not old_avatar == new_avatar:
            if os.path.isfile(old_avatar.path):
                os.remove(old_avatar.path)
    else:
        return False


class Technology(models.Model):
    """ Technology model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
