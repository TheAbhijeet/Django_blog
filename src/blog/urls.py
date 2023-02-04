from django.urls import include, path

from . import views
from blog.views import PostTag
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("tag/<str:tag>/", PostTag.as_view(), name="post_detail"),
]
