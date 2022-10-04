# Django3

## Variable routing

- URL의 일부를 변수로 저장하여 view함수의 인자로 넘길 수 있음
- 하나의 path()에 여러 페이지를 연결시킬 수 있음
- 변수는 <>에 정의하며 view함수의 인자로 할당됨
- str, int, (slug, uuid, path) 5가지 타입

```python
# urls.py

urlpatterns = [
    path('hello/<name>/', views.hello),
]

# articles/views.py
def hello(request, name):
    context = {'name' : name}
    return render(request, 'hello.html', context)
```

```html
<!-- articles/templates/hello.html -->
<h1>만나서 반가워요 {{ name }}님!</h1>
```

## Template inheritance(템플릿 상속)

- 코드의 재사용성

```html
{% extends '' %}
{% block content %}
<!-- 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의 -->
{% endblock content %}
```

- 프로젝트 최상단 template 디렉토리에 위치하기 위해서  

