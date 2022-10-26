from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill

# Create your models here.
class Article(models.Model):
    # Article과 User는 n:1관계, user FK를 넣음
    # accounts 앱에서 User모델 참조
    # user가 탈퇴하면 글도 다 삭제되는걸로
    # settings.AUTH_USER_MODEL로 해도 되는듯
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='images/')
    # If you only want to save the processed image (without maintaining the original)
    # ImageSpecField는 원본도 같이 저장하는듯...
    # ResizeToFill : 설정한 사이즈에 딱 맞춰서 이미지 크기 수정
    # ResizeToFit : 비율 유지한 채로 이미지 크기 수정
    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality':60})
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_articles')
    
class Comment(models.Model):
    # models.ForeighKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                           processors=[ResizeToFill(300, 300)],
                                           format='JPEG',
                                           options={'quality':90})
    
    
