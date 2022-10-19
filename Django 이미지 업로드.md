# Django 이미지 업로드

## 기본 설정

- ImageField

  - FileField를 상속받는 서브 클래스, 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
  - 최대 길이가 100인 문자열로 DB에 생성되며 max_length 인자를 사용하여 최대 길이를 변경할 수 있음

  - (필수) `$ pip install Pillow``

  - ``image = models.ImageField(upload_to='images/', blank=True)`

    - upload_to : 저장할 경로(문자열, 함수) -> MEDIA_ROOT/images/ 경로로 파일 업로드
    - blank : 기본 False, 이미지 필드에 빈 값 허용, DB에 빈 문자열('')이 저장됨
    - null : 기본 False, True일시 빈 값을 DB에 NULL로 저장, Django는 데이터 없음을 빈 문자열로 사용하는 것이 규칙... 그래서 blank=True로 쓰자

  - ```python
    # settings.py
    # 사용자가 업로드 한 미디어 파일들을 보관할 디렉토리의 절대 경로
    # Django는 업로드 파일은 DB에 저장하지 않고, 파일의 경로를 대신 저장
    MEDIA_ROOT = BASE_DIR / 'media'
    # 업로드 된 파일의 URL을 만들어 줌
    MEDIA_URL = '/media/'
    ```

  - `<img src="{{ article.image.url }}" alt="{{ article.image }}">`

  - ```python
    # urls.py
    from django.conf.urls.static import static
    from django.conf import settings
    
    urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ```


## CREATE

- 마이그레이션
- form enctype 속성 지정
  - `<form action="" method='POST', enctype='multipart/form-data'>`
  - multipart/form-data
    - 파일/이미지 업로드 시 반드시 사용
  - application/x-www-form-urlencoded
    - (기본값) 모든 문자 인코딩
  - text/plain
    - 인코딩 하지 않은 문자 상태로 전송
- input요소의 accept 속성 확인
  - `<input type="file" accept="image/*">`

- 업로드 한 파일은 request.FILES 객체로 전달됨
  - `article_form = ArticleForm(request.POST, request.FILES)`
- 실제 파일은 MEDIA_ROOT/images에 저장됨

## READ

- article.image.url == 업로드 파일의 경로, article.image == 업로드 파일의 파일 이름
  - `<img src="{{ article.image.url }}" alt="{{ article.image }}">`

## UPDATE

- 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에 텍스트처럼 일부만 수정하는 것이 불가능하고 새로운 이미지로 덮어 씌워야 함
- enctype 속성 지정 -> request.FILES

## Resizing

- `$ pip install django-imagekit`
- INSTALLED_APP에 imagekit 추가

- ```python
  # models.py
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  class Article(models.Model):
      image = ProcessedImageField(
      	blank=True,
      	processors=[Thumbnail(200, 300)],
      	format='JPEG',
      	options={'quality':90},
      )
  ```

- 
