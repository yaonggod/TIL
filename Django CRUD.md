# Django CRUD

## 1. 시작하기

### 1. 가상환경

```bash
$ python -m venv venv
# 활성화
$ source venv/Scripts/activate
# 비활성화
deactivate
```

### 2. Django 설치

```bash
$ pip install django==3.2.13
# 설치된 패키지 리스트 저장
$ pip freeze > requirements.txt
```

### 3. 프로젝트 생성

```bash
$ django-admin startproject pjt .
```

## 2. articles app

### 1. app 생성

```bash
$ python manage.py startapp articles
```

### 2. app 등록

```python
# project_name/settings.py
INSTALLED_APPS = [
    'articles',
    ...
]
```

### 3. urls.py 설정

```python
# pjt/urls.py
urlpatterns = [
    path('articles/', include('articles.urls')),
]

# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    ...
]
```

- template : `{% url articles:index %}`
- view : `redirect('articles:index')`

## 3. Model 정의(DB 설계)

### 1. 클래스 정의

```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # 최초 저장시에만
    created_at = models.DateTimeField(auto_now_add=True)
    # save() 할때마다
    updated_at = models.DateTimeField(auto_now=True)
```

### 2. 마이그레이션 파일 생성

```bash
$ python manage.py makemigrations
```

### 3. 마이그레이트(DB반영)

```bash
$ python manage.py migrate
```

## 4. CRUD

### 1. ModelForm 선언

```python
# articles/forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
```

### 2. 게시글 생성

```python
# articles/views.py
from .forms import ArticleForm

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            # POST로 들어오고 유효성 검사를 통과하면 글을 생성
            article_form.save()
            # index로 redirect
            return redirect('articles:index')
    else:
    	article_form = ArticleForm()
    # POST가 아니거나 유효성 검사를 통과하지 못하면
    context = {'article_form' : article_form,}
    # create로 다시 돌아옴
    return render(request, 'articles/create.html', context=context)
```

```html
<!-- articles/create.html -->
<form action="" method="POST">
    <!-- CSRF 공격을 막는 토큰 -->
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type="submit" value="글쓰기">
</form>
```

