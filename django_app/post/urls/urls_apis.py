from django.conf.urls import url

from post import apis

urlpatterns = [
    url(r'^$', apis.PostListView.as_view()),
]