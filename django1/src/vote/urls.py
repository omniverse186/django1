'''
Created on 2019. 1. 20.

@author: user
'''
#하위 URLConf
#app_name : 하위 URLConf 파일의 등록된 URL들의 그룹명
#urlpatterns : URL과 뷰함수를 리스트 형태로 등록하는 변수
from django.urls import path 
from .views import *

app_name = 'vote'
urlpatterns = [
    #name : 해당 URL, 뷰함수 등록에 대해서 별칭을 지정
    path('', index, name= 'index'),
    path('<int:q_id>/', detail, name='detail'),
    path('vote/', vote, name='vote'),
    path('result/<int:q_id>',result, name='result'),
    path('qr/', qregister, name='qr' ),
    path('qu/<int:q_id>/', qupdate, name = 'qu'),
    path('qd/<int:q_id>/', qdelete, name='qd'),
    path('cr/', cregister, name='cr'),
    path('cu/<int:c_id>/', cupdate, name='cu'),
    path('cd/<int:c_id>/', cdelete, name='cd')
    ]