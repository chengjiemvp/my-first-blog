from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    #登陆视图函数
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))
#注册视图函数,成功之后自动登陆，需要导入login，authenticate认证函数，默认表单UserCreationForm
def register(request):
    '''注册新用户'''
    if request.method != 'POST':
        #显示空的表单
        form = UserCreationForm()
    else:
        #处理填好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            #让用户自动登陆
            authenticate_user = authenticate(
                    username=new_user.username,
                    passwd=request.POST[passwd1]
                    )
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('blog:index'))
    context = {'form':form}
    return render(request,'users/register.html',context)
