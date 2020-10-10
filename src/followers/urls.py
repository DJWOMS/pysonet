from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>', views.FollowerView.as_view()),
    path('', views.ListFollowerView.as_view())
]
