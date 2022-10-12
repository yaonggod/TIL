from django.shortcuts import render, redirect
from .models import Article 
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context=context)

# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form' : article_form
#     }
#     return render(request, 'articles/new.html', context=context)

def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Article.objects.create(title=title, content=content)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            # POST로 받아오고 유효성 검사를 통과하면 입력한 글을 저장하고
            article_form.save()
            # index로 redirect한다
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form
    }
    # POST가 아니거나 POST에서 유효성 검사를 통과하지 못하면 다시 new로 돌아간다
    return render(request, 'articles/new.html', context=context)    
    
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)    

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 값 가져와서 검증하고 DB에 저장
        # instance는 원래 article 값 넣어두는거 같은데
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)  
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form
    }
    # POST가 아니거나 POST에서 유효성 검사를 통과하지 못하면 다시 new로 돌아간다
    return render(request, 'articles/update.html', context=context)