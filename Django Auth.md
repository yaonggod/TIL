# Django Auth

- Django authentication system은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공(처리)하고 있음
  - User
  - 권한 및 그룹
  - 암호 해시 시스템
  - Form 및 View 도구
  - 기타 적용가능한 시스템
- 필수 구성은 settings.py의 INSTALLED_APPS - django.contrib.auth
- Authentication(인증) - 신원 확인
- Authorization(권한, 허가) - 권한 부여
- 사전 설정
  - accounts app 생성 및 등록
  - url 분리 및 매핑

## User model 활용하기

- User 모델 정의 - 기본 User 모델이 충분하더라도 커스텀 User 모델 설정하는 것을 강력히 권장

  - models에서` from django.contrib.auth.models import AbstractUser`

  - settings.py - `AUTH_USER_MODEL = 'auth.User'`를 `'accounts.User'`로 대체
  - admin.py에 커스텀 User 모델 등록
    - `from django.contrib.auth.admin import UserAdmin`
    - `admin.site.register(User, UserAdmin) `

- 데이터베이스 초기화

  - migration 파일 삭제 -> db.sqlite3 삭제 -> migration 진행

- User객체

  - 기본 속성 : username, password, email, first_name, last_name
  - user 생성
    - `user = User.objects.create_user('john', 'john@google.com', '129u31i23')`
  - 비밀번호  변경
    - `user.set_password('dsklfjdsklfs')`
    - `user.save()`
  - user인증
    - `from django.contrib.auth import authenticate`
    - `user = authenticate(username = 'john', password = 'sdfjkldsfjls')`

- 암호 관리
  - Django에서는 기본적으로 PBKDF2(Password-based Key Derivation Function)를 사용하여 암호 저장
    - 단방향 해시함수를 활용해 비밀번호를 다이제스트로 암호화, Django는 SHA256활용
    - 보완책
      - 솔팅(salting) - 임의의 문자열 salt를 추가해 다이제스트 생성 
      - 키 스트레칭(Key Stretching) - 해시를 여러 번 반복해 시간을 늘림

## 회원 가입

- UserCreationForm

  - 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

  ```python
  class UserCreationForm(forms.ModelForm):
      class Meta:
          model = User
          fields = ('username', )
          field_classes = {'username' : UsernameField}
  
  from django.contrib.auth.forms import UserCreationForm
  
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = UserCreationForm()
      context = {'form' : form}
      return render(request, 'accounts/signup.html', context)
      
  ```

  이렇게 하면 에러가 남...

  UserCreationForm이 기존 유저 모델로 작성된 클래스라서, 우리가 대체한 커스텀 유저 모델이 아님 -> 기존 UserCreationForm을 상속받아 User모델 재정의

  ```python
  from django.contrib.auth import get_user_model
  from django.contrib.auth.forms import UserCreationForm
  
  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
          model = get_user_model
  ```

  그리고 views의 UserCreationForm을 CustomUserCreationForm으로 대체하기

  

