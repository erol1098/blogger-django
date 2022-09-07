from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import CommentForm, PostForm
from .models import Post
# Create your views here.

def post_list(request):
  posts = Post.objects.all()

  ctx = {"posts":posts}

  return render(request, "blog/post_list.html", ctx)


def post_create(request):

  form = PostForm()

  if request.method == "POST":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      print(request.POST)
      form.save()
      return redirect("index")

  ctx = {"form":form}
  
  return render(request, "blog/post_create.html", ctx)


def post_update(request,id):

  post = Post.objects.get(id=id)
  print(post)
  form = PostForm(instance=post)

  if request.method == "POST":
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
      return redirect("index")

  ctx = {"form":form}
  
  return render(request, "blog/post_update.html", ctx)



def post_delete(request, id):
  post = Post.objects.get(id=id)
  if request.method == "POST":
    post.delete()
    return redirect("index")

  posts = Post.objects.all()
  ctx = {"posts":posts}
  
  return render(request,"blog/post_delete.html",ctx)



def post_detail(request,id):
  post = Post.objects.get(id=id)
  commentForm = CommentForm()
  if request.method =="POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      form.save()
      form.clean()

  ctx = {"post":post,"form":commentForm}
  
  return render(request, "blog/post_detail.html", ctx)