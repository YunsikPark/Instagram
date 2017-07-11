from django.conf.urls import url, include

from . import urls_apis, urls_views
urlpatterns = [
    url(r'^', include(urls_views)),
    url(r'^api/', include(urls_apis)),
    # /....은 url_views.py 의  urls_views 모듈 사용
    # /apis/...은 urls_apis 모듈 사용
]