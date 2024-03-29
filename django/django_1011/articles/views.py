from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
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
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            # POST로 받아오고 유효성 검사를 통과하면 입력한 글을 저장하고
            article = article_form.save(commit=False)
            article.user = request.user
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
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comments' : comments,
        'comment_form' : comment_form
    }
    return render(request, 'articles/detail.html', context)    

@ login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            # POST : input 값 가져와서 검증하고 DB에 저장
            # instance는 원래 article 값 넣어두는거 같은데
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
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

@ login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', pk)
    else:
        comment_form = CommentForm()
    context = {'comment_form' : comment_form}
    return render(request, 'articles/detail.html', context)

@ login_required
def comment_update(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('articles:detail', article_pk)
    return redirect('articles:detail', article_pk)    
    
    
@ login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        if comment.user == request.user:
            comment.delete()
            return redirect('articles:detail', article_pk)
    return redirect('articles:detail', article_pk)

@login_required
def like(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in article.like_users.all(): 
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가하고 
        article.like_users.add(request.user)
    # 상세 페이지로 redirect
    return redirect('articles:detail', article_pk)

            
