from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.UserNetPrivateView.as_view()),
    path('profile/avatar/', views.UserNetAvatarView.as_view()),
    path('profile/avatar/base64/', views.UserNetAvatarBase64View.as_view()),
    path('profile/<int:pk>/', views.UserNetPublicView.as_view({'get': 'retrieve'})),
]
