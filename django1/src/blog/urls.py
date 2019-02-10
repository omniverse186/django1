'''
Created on 2019. 2. 9.

@author: user
'''
from .views import *
from django.urls import path
app_name = 'blog'

urlpatterns = [
    #뷰클래스 등록시 뷰클래스.as_view로 등록
        path('', Index.as_view(), name='index'),
        path('<int:pk>/',Detail.as_view(), name='detail'),
        path('posting/',Posting.as_view(), name='posting')
    ]