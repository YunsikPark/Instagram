from django.conf.urls import url

from . import views

urlpatterns = [
    # url() 사용법
    # https://docs.djangoproject.com/en/1.11/ref/urls/#url
    # /post/$
    url(r'^$', views.post_list, name = 'post_list'),

    # post_detail과 매칭
    # /post/3/$, /post/5/$
    # 정규표현식에서 매칭된 그룹을 위치 인수로 반환하는 방법
    # url(r'^(\d+)/$',views.post_detail, name='post_detail'),

    # 정규 표현식에서 매칭된 그룹을 키워드 인수로 반환하는 방법
    # 그룹의 가장 앞 부분에 ?P<패턴이름을 지정
    url(r'^(?P<post_pk>\d+)/$',views.post_detail, name='post_detail'),
]
