'''定义blog的URL模式'''
from django.conf.urls import url

from . import views

urlpatterns=[
        #主页
        url( r'^$',views.index, name = 'index' ),
        #发表文章的页面
        url( r'^new_article/$', views.new_article, name = 'new_article' ),
        #编辑文章的页面
        url(r'^edit_article/(?P<post_id>\d+)/$',views.edit_article,name='edit_article'),
        #查看文章的页面
        url(r'^look_over_article/(?P<post_id>\d+)/$',views.look_over_article,
            name='look_over_article'),
        ]
