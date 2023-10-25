from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now=datetime.now()
    return render(request,'index.html',locals())
def showpost(request,slug):
    post=Post.objects.get(slug=slug)#selet*from post where slug=%slug
    if post != None:
        return render(request,'post.html',locals())
    else:
        return redirect("/")
    #select * from post where slug=%slug
'''
def homepage(request):
    posts = Post.objects.all()#select*from post
    post_lists=list()
    for counter,post in enumerate(posts):#enumerate 
        post_lists.append(f'No.{counter} {post} <br>')#br換行
    return HttpResponse(post_lists)
'''