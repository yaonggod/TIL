from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles' : articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/detail.html', {'article' : article})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    return render(request, 'articles/create.html', {'form' : form})

def update(request, pk):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=Article.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=Article.objects.get(pk=pk))
    return render(request, 'articles/update.html', {'form' : form})

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', pk)        
