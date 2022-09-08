from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User

from .forms import CommentForm, PostForm
from .models import Post, PostView
# Create your views here.

def post_list(request):
  posts = Post.objects.all()

  ctx = {"posts":posts}

  return render(request, "blog/post_list.html", ctx)

@login_required(login_url='/user/login/')
def post_create(request):
  user = User.objects.get(id=request.user.id)
  form = PostForm()

  if request.method == "POST":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      
      post = form.save(commit=False)
      post.author = user
      post.save()
    
      return redirect("index")

  ctx = {"form":form}
  
  return render(request, "blog/post_create.html", ctx)

@login_required(login_url='/user/login/')
def post_update(request,id):

  post = Post.objects.get(id=id)
  form = PostForm(instance=post)

  if request.method == "POST":
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
      
      return redirect("index")

  ctx = {"form":form}
  
  return render(request, "blog/post_update.html", ctx)


@login_required(login_url='/user/login/')
def post_delete(request, id):
  post = Post.objects.get(id=id)
  if request.method == "POST":
    post.delete()
    return redirect("index")

  posts = Post.objects.all()
  ctx = {"posts":posts}
  
  return render(request,"blog/post_delete.html",ctx)


@login_required(login_url='/user/login/')
def post_detail(request,id):
  user = User.objects.get(id=request.user.id)
  post = Post.objects.get(id=id)
  form = CommentForm()

  pw = PostView(viewer=user, post=post)
  pw.save()
  
  query = PostView.objects.filter(post=post)
  viewCount = len(query)

  if request.method =="POST":
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.author = request.user
      comment.save()
      return redirect(f"/detail/{id}")  


  ctx = {"post":post,"form":form, "viewCount":viewCount}
  
  return render(request, "blog/post_detail.html", ctx)