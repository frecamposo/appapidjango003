from django.urls import re_path as path
from .views import PostViewSet,PostSearchSet

urlpatterns = [
    path(r'^api/post/$', PostViewSet.as_view()),
    path(r'^api/post/(?P<id>.+)/$', PostSearchSet.as_view()),
]
