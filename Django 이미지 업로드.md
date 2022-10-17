# Django 이미지 업로드

- `$ pip install Pillow`
- `image = models.ImageField(upload_to='images/', blank=True)`
- `<form method='POST', enctype='multipart/form-data'>`
- `article_form = ArticleForm(request.POST, request.FILES)`
- `<img src="{{ article.image.url }}" alt="{{ article.image }}">`

```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'images'
MEDIA_URL = '/media/'

# urls.py
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- `$ pip install django-imagekit`
- 

