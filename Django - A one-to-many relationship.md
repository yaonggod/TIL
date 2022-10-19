# Django - A one-to-many relationship

- 외래 키 : 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 필드
- RDB에서의 관계
  - 1:1 - 사용자:프로필
  - 1:N - 사용자의 글 :댓글
  - M:N

## Foreign Key

- 참조 무결성
- ForeignKey(to(참조하는 model class), on_delete)
  - on_delete : 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리?
    - CASCADE : 부모 객체 삭제 시 참조하는 객체도 삭제
    - PROTECT, SET_NULL, SET_DEFAULT....
  - 참조하는 모델의 단수형으로 필드를 만드는 걸 권장
  - 

## 1:N(Article-Comment)

- 게시글은 여러 개(0 ~ N)의 댓글을 가진다
- 댓글은 반드시 하나의 게시글에 속한다

- Comment - id/content/created_at/updated_at/article_id

- Article - id/title/content/created_at/updated_at

- 기존 Articles 앱에서... 댓글은 게시글에 종속된 것

  - 댓글 목록 : articles/detail
  - 댓글 작성 : articles/detail
  - 댓글 생성 : DB 저장 후 detail 페이지 리다이렉트

- Model

  -  id/content/created_at/updated_at/article_id(FK)

  ```python
  class Comment(models.Model):
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      article = models.ForeignKey('Article', on_delete=models.CASCADE)
  ```

- 참조 : `Comment.objects.filter(article_id = 13)`
- 역참조 : `article.comment_set.all()`

```python
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comments' : comments,
        'comment_form' : comment_form
    }
    return render(request, 'articles/detail.html, context')
```

