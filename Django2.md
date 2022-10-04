# Django2

## 요청과 응답

- URL -> VIEW -> TEMPLATE
- URLs

```python
# urls.py
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```

- Views - HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성

```python
# articles/views.py
def index(request):
    return render(request, 'index.html')
```

- render()

  - 주어진 템플릿을 주어진 context 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수
    - request : 응답을 생성하는 데 사용하는 요청 객체
    - template_name : 템플릿의 전체 이름 또는 템플릿 이름의 경로
    - context : 템플릿에서 사용할 데이터 (딕셔너리 타입)

- Templates - 실제 내용을 보여주는데 사용되는 파일

  - 기본 경로 : `app_name/templates/index.html`

- 추가 설정

  ```python
  # settings.py
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  # 시간대 인식 여부
  USE_TZ = True
  ```

## Django Template

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입
- Django Template Language
  - 조건, 반복, 변수 치환, 필터 등의 기능 제공
  - 파이썬 코드로 실행되는 것이 아님
  - 프로그래밍적 로직이 아닌 프레젠테이션을 표현하기 위한 것

- Variable
  - `{{ variable }}`
  - 영어, 숫자, _의 조합으로 구성되나 _로 시작하지는 못함, 공백 구두점 불가
  - .을 사용해 변수 속성에 접근할 수 있음
    - 인덱싱 `{{ foods.0 }}`
    - 키값으로 접근 `{{ info.name }}`
  - render()의 세번째 인자로 {'key' : value}와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
- Filters
  - `{{ variable|filter }}`
  - 표시할 변수를 수정할 때 사용
    - `{{ pick|length }}`
    - `{{ foods|join: ', '}}`
    - `{{ name|lower }}` :  name 변수를 모두 소문자로 출력
  - chained가능
- Tags
  - 출력 텍스트를 만들거나 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
  - `{% if %} {% endif %} 처럼 시작 태그와 종료 태그가 필요한 경우가 있음
- Comments
  - 주석
  - `{# #}`
  - `{% comment %} {% endcomment %}`