'''
Created on 2019. 1. 27.

@author: user
'''
from django.urls import path
from .views import *

app_name = 'cl'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout')
    ]