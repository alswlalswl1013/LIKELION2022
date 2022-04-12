from tabnanny import process_tokens
from django.shortcuts import render, redirect
from .models import Post
from datetime import datetime
# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('deadline')
    post_data = []
    for post in posts:
        remain = post.deadline.replace(tzinfo=None) - datetime.now()
        data = {
            'pk': post.pk,
            'title': post.title,
            'remain': remain
        }
        post_data.append(data)

    return render(request, 'home.html', {'posts': post_data})


def new(request):
    if request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
        )
        return redirect('home')
    return render(request, 'new.html')


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post': post})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post': post})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')
