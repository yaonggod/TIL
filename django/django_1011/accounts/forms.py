from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# 비밀번호 두개를 받아서 일치하는 로직이 포함된 폼
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'last_name', 'first_name')
        help_texts = {
            'username' : '',
            'email' : '',
            'password' : '' 
        }

# 비밀번호 두 개를 받을 필요가 없는 폼?
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'last_name', 'first_name')
        