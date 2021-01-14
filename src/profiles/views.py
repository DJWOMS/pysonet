import base64
import os

from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics, response, mixins
from PIL import Image

from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer, GetUserNetAvatarSerializer
import uuid


class UserNetPublicView(ModelViewSet):
    """ Вывод публичного профиля пользователя
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetPrivateView(generics.RetrieveUpdateAPIView):
    """ Вывод профиля пользователя
    """
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj


class UserNetAvatarView(generics.RetrieveUpdateDestroyAPIView):
    """ Изменение аватара пользователя
    """
    serializer_class = GetUserNetAvatarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj

    def put(self, request, *args, **kwargs):
        max_weight = 1048576
        min_size = 100
        max_size = 5000
        try:
            avatar = request.data["avatar"]
            image = Image.open(avatar)
            (width, height) = image.size
            if avatar.size > max_weight:
                return response.Response({"error": "Please upload a picture smaller than 1 MB."}, status=400)
            elif width and height < min_size:
                return response.Response({"error": "Please upload a picture bigger than {}x{}."
                                         .format(min_size, min_size)}, status=400)
            elif width and height > max_size:
                return response.Response({"error": "Please upload a picture smaller than {}x{}."
                                         .format(max_size, max_size)}, status=400)
            # можно удалить старую аватарку без сигналов
            # else:
            #     image = request.user.avatar.path
            #     if os.path.exists(image):
            #         os.remove(image)
            #     else:
            #         return response.Response({"error": "File does not exists."}, status=400)
        except KeyError:
            response.Response(status=400)
        return self.update(request, avatar=avatar)


class UserNetAvatarBase64View(generics.RetrieveUpdateDestroyAPIView):
    """ Изменение аватара в формате Base64 пользователя
    """
    serializer_class = GetUserNetAvatarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj

    def put(self, request, *args, **kwargs):
        try:
            avatar = request.data["avatar"]
            if 'data:' in avatar and ';base64,' in avatar:
                header, avatar = avatar.split(';base64,')
            data = base64.b64decode(avatar)
            file = ContentFile(data)
            request.user.avatar.save('{}.jpg'.format(uuid.uuid1()), file, save=True)
        except KeyError:
            return response.Response({"error": "error"}, status=400)
        return response.Response({"message": "ok"}, status=200)
