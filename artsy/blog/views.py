from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post,Category,Slideshow,Message
from django.views.generic import (
    TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



def AboutView(request):
    posts = Post.objects.filter(pin_to_bio=True)
    slideshow = Slideshow.objects.all()
    messages = Message.objects.all()
    return render(request,'about_page.html',{'posts':posts,'slideshow':slideshow,'messages':messages})


def PostListView(request):
    category = request.GET.get('category')
    if category==None:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(category__name=category)
    categories = Category.objects.all()
    return render(request,'blog/post_list.html',{'categories':categories,'posts':posts})

def PostDetailView(request,pk):
    category = request.GET.get('category')
    if category==None:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(category__name=category)
    categories = Category.objects.all()
    post = Post.objects.get(pk=pk)
    return render(request,'blog/post_detail.html',{'categories':categories,'post':post})
