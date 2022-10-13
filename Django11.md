# Django 11

## 회원정보 수정

- UserChangeForm
  - 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
  - UserChangeForm 또한 ModelForm이기 때문에 instance인자로 기존 user 데이터 정보를 받는 구조 또한 동일함
  - CustomUserChangeForm 사용

```python
# form.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 수정하고자 하는 필드
        fields = ('email', 'first_name', 'last_name')

# urls.py
path('update/', views.update, name='update'),

# views.py
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form, }
    return render(request, 'accounts/update.html', context)
```

## 비밀변호 변경

- PasswordChangeForm
  - 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있는 Form
  - 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

```python
# urls.py
path('password/', views.change_password, name='change_password')

# views.py
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 여기까지 하면 변경 후 로그인 상태가 지속되지 못함
            # 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 불일치하여 로그인 정보 유지 불가
            # 새로운 password의 session data로 session 업데이트
            update_session_auth_hash(request, form.user)
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form, }
    return render(request, 'accounts/change_password.html', context)
```

## 탈퇴

```python
# views.py
def delete(request):
    # 1. 탈퇴
    request.user.delete()
    # 2. 로그아웃 : 먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어져서 탈퇴가 안됨
    auth_logout(request)
    return redirect('articles:index')
```

