from django.shortcuts import render, redirect
from .models import Post, Comment

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

    if request.method=='POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content
        )
        return redirect('detail_page',post_pk)
    return render(request, 'detail_page.html', {"post":post})

def delete_comment(request, post_pk, comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail_page',post_pk)