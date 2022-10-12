# Django8

## Static Files

- 웹 서버는 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서 제공하는 응답(HTTP response)을 처리하는 것을 기본 동작으로 함
- 즉 웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원(static resource)을 제공

- 정적 파일
  - 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  - 웹 서버는 일반적으로 이미지, 자바스크립트 또는 CSS와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야 함
  - django.contrib.staticfiles 앱을 통해 정적 파일과 관련된 기능 제공
- 정적 파일 활용
  - django.contrib.staticfiles가 INSTALLED_APPS에 포함되어 있는지 확인
  - settings.py에서 STATIC_URL을 정의
  - 앱의 static 디렉토리에 정적 파일 저장

```html
{% load static %}
<img src="{% static img.jpg %}">
```

