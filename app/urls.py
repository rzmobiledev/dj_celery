from django.urls import path

from app.views import (UserView, UserViewDetail,
                       ArticleView, ArticleViewDetailAndUpdate)

app_name = 'user'

urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('<int:pk>/', UserViewDetail.as_view(), name='user-detail'),
    path('article/', ArticleView.as_view(), name='article'),
    path('article/<int:pk>', ArticleViewDetailAndUpdate.as_view(),
         name='article-detail'),
]
