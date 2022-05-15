from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def list_page(request):
    posts = Post.objects.all()
    return render(request, 'list_page.html', {'posts':posts})

def create_page(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],

        )
        return redirect('detail_page', new_post.pk)
    return render(request, 'create_page.html')

def edit_page(request, post_pk):
    post=Post.objects.filter(pk=post_pk)
    if request.method == 'POST':
        post.update(
            title=request.POST['title'],
            content=request.POST['content'],
        )
        return redirect('detail_page.html', post.pk)
    return render(request, 'edit_page.html', {'post':post[0]})

def delete(request, post_pk):
    Post.objects.filter(pk=post_pk).delete()
    return redirect('list_page')

def detail_page(request, post_pk):
    post=Post.objects.get(pk=post_pk)
    post.view +=1
    post.save()
    return render(request, 'detail_page.html', {"post":post})