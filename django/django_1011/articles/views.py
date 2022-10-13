from django.shortcuts import render, redirect
from .models import Article 
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# accouts 앱에서 User모델 참조
from accounts.models import User

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context=context)

# 로그인이 되어있지 않으면 로그인 페이지로 리다이렉트
@ login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            # POST로 받아오고 유효성 검사를 통과하면 입력한 글을 저장하고
            article = article_form.save(commit=False)
            article.user = request.user
            article.user_name = User.objects.get(pk=request.user.pk).username
            article.save()
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

@ login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            # POST : input 값 가져와서 검증하고 DB에 저장
            # instance는 원래 article 값 넣어두는거 같은데
            article_form = ArticleForm(request.POST, instance=article)
            if article_form.is_valid():
                article_form.save()
                return redirect('articles:detail', article.pk)  
        else:
            article_form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article_form' : article_form
    }
    # POST가 아니거나 POST에서 유효성 검사를 통과하지 못하면 다시 new로 돌아간다
    return render(request, 'articles/update.html', context=context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)