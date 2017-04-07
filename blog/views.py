from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

# Create your views here.
@login_required
def index(request):
    '''个人博客的主页，显示所有文章'''
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    for post in posts:
        post.text=post.text[:222]+'.........'
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
            #在这里，因为post必须要有author这个主键，所以我们在保存前不提交，而是用另一个
            #form_add来添加键然后再保存。
            form_add = form.save(commit=False)
            form_add.author=request.user
            form_add.published_date=timezone.now()
            form_add.save()
            return HttpResponseRedirect(reverse('blog:index'))
    context={'form':form}
    return render(request,'blog/new_article.html',context)
def edit_article(request,post_id):
    '''编辑已发表的文章'''
    post = Post.objects.get(id=post_id)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        #填写了数据,POST提交的数据
        form = PostForm(instance=post,data=request.POST)#这里面的instance和data都不能少，不写instance会导致更改文章就相当与添加了一篇新的文章。
        if form.is_valid():
            form_add = form.save(commit=False)
            form_add.author=request.user
            form_add.published_date=timezone.now()
            form_add.save()
            return HttpResponseRedirect(reverse('blog:index'))
    context={'post':post,'form':form}
    return render(request,'blog/edit_article.html',context)

def look_over_article(request,post_id):
    '''查看文章'''
    post=Post.objects.get(id=post_id)
    return render(request,'blog/look_over_article.html',{'post':post})
