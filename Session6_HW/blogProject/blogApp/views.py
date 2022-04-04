from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def new(request):
    if request.method =='POST':
        category=request.POST['category']
        
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content=request.POST['content'],
            # create_time=request.POST['create_time'],
            category=request.POST['category']
        )
        return redirect('list')
    return render(request, 'new.html')

def list(request):
    hobby_len = len(Article.objects.filter(category='hobby'))
    food_len = len(Article.objects.filter(category='food'))
    programming_len = len(Article.objects.filter(category='programming'))
    return render(request, 'list.html', {'hobby_len':hobby_len, 'food_len': food_len, 'programming_len': programming_len})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})

def category(request, category):
    articles=Article.objects.filter(category=category)
    return render(request, 'category.html',{'articles':articles})