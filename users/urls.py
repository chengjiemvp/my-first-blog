#别忘了导入模块
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns=[
        #登陆页面
        url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
        #注册视图
        url(r'^register/$',views.register,name='register'),
        #注销视图
        url(r'^logout/$',views.logout_view,name='logout'),
        ]
