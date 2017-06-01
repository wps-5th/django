from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
# 시작파트부터 뭔가 오고 뒤에 vote/로 끝맺음 되는 친구들인데 시작파트는 ( ) 를 통해 그룹지어주고 ?P 로 이름을 정의해준다
# <지을 이름> 뒤로 [0-9]+ 아무 숫자의 나열이 온다.