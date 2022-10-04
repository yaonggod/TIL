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

- 프로젝트 최상단 template 디렉토리에 위치하기 위해서 다음과 같이 코드 작성

```python
# settings.py
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates',],
    }
]
```

## Sending and Retrieving form data

- 웹은 기본적으로 클라이언트-서버 아키텍처를 사용
- 클라이언트 측에서 HTML form은 HTTP요청을 서버에 보내는 가장 편리한 방법

### Sending form data(Client)

- HTML <form> element
  - 데이터가 전송되는 방법을 정의
  - 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
  - 데이터를 어디(action)로 어떤 방식(method)으로 보낼지
    - action : 입력 데이터가 전송될 URL, 지정하지 않으면 현재 form이 있는 페이지의 URL로 보내짐
    - method : HTML form 데이터는 오직 GET, POST로만 전송 가능
- HTML <input> element
  - 사용자로부터 데이터를 입력받기 위해 사용
  - type 특성에 따라 input 요소의 동작 방식이 달라짐, 기본값은 text
  - name
    - form을 통해 데이터를 제출(submit)했을 때 name속성에 설정된 값을 서버로 전송하고, 서버는 name속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
    - 주요 용도는 GET/POST방식으로 서버에 전달하는 파라미터(name = key, value = value)로 매핑하는 것

```python
# urls.py
urlpatterns = [path('throw/', views.throw),]

# views.py
def throw(request):
    return render(request, 'throw.html')
```

```html
<!-- throw.html -->
<form action="#" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
</form>
```

- HTTP request methods
  - 주어진 자원에 수행하길 원하는 행동
  - GET, POST, PUT, DELETE
  - GET 
    - 서버에게 리소스를 요청하기 위해 사용
    - 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
      - Query String Parameters : url 주소에 데이터를 파라미터를 통해 넘기는 것
      - http://host:port/path?key=value&key=value

### Retrieving the data(Server)

- 데이터 가져오기(검색하기)
- 서버는 클라이언트로 받은 key-value쌍의 목록과 같은 데이터를 받게 됨

```html
<!-- throw.html -->
<form action="/catch/" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
</form>

<!-- index.html -->
<a href="/throw/">throw</a>
```

```python
# views.py
def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)
```

```html
<!-- catch.html -->
<h1>여기서 {{ message }}를 받았어!</h1>
<a href="/throw/">다시 던져!</a>
```

- 요청과 응답 객체 흐름
  1. 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
  2. 그리고 해당하는 적절한 view함수를 로드하고 HttpRequest를 첫번째 인자로 전달
  3. 마지막으로 view함수는 HttpResponse object를 반환

## Django URLs

- Django는 URL끝에 /가 없다면 자동으로 붙여주는 것이 기본 설정
- 기술적으로 foo.com/bar와 foo.com/bar/는 서로 다른 URL
- Django는 URL을 정규화하여 검색 엔진이 혼동하지 않도록 함
