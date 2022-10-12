# Django Login

## HTTP

- 비연결지향
- 무상태
- 어떻게 로그인 상태를 유지?
- 쿠키
  - 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
  - 세션 관리, 개인화, 트래킹
  - 쿠키 수명
- 세션
  - 사이트와 특정 브라우저 사이의 상태를 윶시키는 것
  - session id

- 세션 관리
- 

## 로그인

- url GET/accounts/login -> 로그인 폼 제공
- url POST/accounts/login -> 로그인 처리, 게시글 목록 페이지로 redirect
- from django.contrib.auth.forms import AuthenticationForm - ModelForm이 아님
- form = AuthenticationForm(request, data=request.POST)
- form.is_valid(): login(request, form.get_user())
- from django.contrib.auth.decorators import login_required
- from django.contrib.auth import logout