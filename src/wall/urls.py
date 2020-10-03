from django.urls import path
from . import views


urlpatterns = [
    path('comment', views.CommentsView.as_view({'post': 'create'})),
    path('comment/<int:pk>', views.CommentsView.as_view({'put': 'update', 'delete': 'destroy'})),
    path('post', views.PostView.as_view({'post': 'create'})),
    path('post/<int:pk>', views.PostView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('<int:pk>', views.PostListView.as_view()),
]
