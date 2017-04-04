'''定义blog的URL模式'''
from django.conf.urls import url

from . import views

urlpatterns=[
        #主页
        url( r'^$',views.index, name = 'index' ),
        url( r'^new_article/$', views.new_article, name = 'new_article' ),
        ]
