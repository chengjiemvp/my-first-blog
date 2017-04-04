from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    '''个人博客的主页'''
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date'
            )
    return render(request,'blog/index.html',{'posts':posts})
def new_article(request):
    '''发布新文章'''
    if request.method != 'POST':
        #未提交数据，创建一个新表单供用户填写
        form = PostForm()
    else:
        #填写了数据，POST提交的数据
        form = PostForm(request.POST)
        if form.is_valid():
            #在这里，因为post为
            form_add = form.save(commit=False)
            form_add.author=request.user
            form_add.published_date=timezone.now()
            form_add.save()
            return HttpResponseRedirect(reverse('blog:index'))
    context={'form':form}
    return render(request,'blog/new_article.html',context)
