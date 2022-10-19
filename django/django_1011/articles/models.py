from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # Article과 User는 n:1관계, user FK를 넣음
    # accounts 앱에서 User모델 참조
    # user가 탈퇴하면 글도 다 삭제되는걸로
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    # models.ForeighKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
    
    
