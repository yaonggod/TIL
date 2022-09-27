from django.shortcuts import render
from .models import Article

contents = []

# Create your views here.
def index(request):
    # DB에서 가져오기
    contents = Article.objects.all()
    context = {
        'contents' : contents
    }
    # SELECT * FROM articles;
    return render(request, 'articles/index.html', context)

def create(request):
    content = request.GET.get('content')
    # contents.append(content)
    # DB에 저장
    Article.objects.create(content = content)
    context = {
        'content' : content
    }
    return render(request, 'articles/create.html', context)