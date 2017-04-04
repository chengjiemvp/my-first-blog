from django.shortcuts import render

# Create your views here.
def index(request):
    '''个人博客的主页'''
    return render(request,'blog/index.html')
