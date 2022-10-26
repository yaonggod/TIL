# M:N

- N:1의 한계
- 예) 한 명의 의사에게 여러 환자가 예약

```python
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()
```

- 그런데 동시에 예약할 수 없나? -> 환자 객체를 여러 개 만들어서 하는 수 밖에, 외래 키는 Integer 타입으로만 받으므로 동시에 받을 수 없음

```python
patient = Patient.objects.create(name='carol', doctor=doctor1, doctor2)
```

- 환자 모델의 FK를 삭제하고 예약 모델을 새로 만들기

```python
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

- 예약 정보 조회

```python
doctor1.reservation_set.all()
patient1.reservation_set.all()
```

- 환자 모델에 ManytoManyField 작성 -> ManytoManyField를 통해 중개 테이블을 자동으로 생성
- related_name
  - target model이 source model을 참조할 때 사용할 manager name

```python
class Patient(models.Model):
    doctors = models.ManytoManyField(Doctor, related_name='patients')
    name = models.TextField()
```

- 중개 테이블에 hospitals_patient_doctors 생성
- 의사, 환자 생성

```python 
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')

# 예약
patient1.doctors.add(doctor1)
# related_name을 설정하면 doctor1.patient_set.add(patient2) 못씀
doctor1.patients.add(patient2)
patient1.doctors.all()
doctor1.patients.all()

# 취소
doctor1.patient_set.remove(patient1)
patient2.doctors.remove(doctor1)
```

- 중개 모델을 직접 작성하는 경우 -> through 옵션을 사용해 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음

```python
class Patient(models.Model):
    doctors = models.ManytoManyField(Doctor, through='Reservation')
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
```

## ManytoManyField

- `ManytoManyField(to, **options)`

-  다대다 관계 설정 시 사용하는 모델 필드

- 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요

- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음

  - `add() `- 지정된 객체를 관련 객체 집합에 추가
  - `remove()` - 관련 객체 집합에서 지정된 모델 개체를 제거
  - `create()`
  - `clear()`

- Django는 다대다 관계를 나타내는 중개 테이블을 만듦

- 테이블 이름은 ManytoManyField 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성됨

- 'db_table' arguements을 활용하여 중개 테이블의 이름을 변경할 수도 있음

- Arguments

  - related_name - target model이 source model을 참조할 때 사용할 manager name

  - through - 중개 테이블을 직접 작성하는 경우 중개 테이블을 나타내는 argument

  - symmetrical

    - default : True
    - ManytoManyField가 동일한 모델을 가리키는 정의에서만 사용
    - True일시
      - _set 매니저를 추가하지 않음
      - 대칭적 관계 형성

    ```python
    class Person(models.Model):
        friends = models.ManytoManyField('self')
    ```

- 중개 테이블 필드 생성 규칙
  - 소스와 대상이 다른 경우 - id/patient_id/doctor_id
  - 동일한 모델을 가리키는 경우 - id/from_person_id/to_person_id

## Article-User

```python
class Article(models.Model):
    ...
    like_users = models.ManytoManyField(settings.AUTH_USER_MODEL)
    ...
```

- article_set 중첩 문제
  - user.article_set이 user가 작성한 글들인지 user가 좋아요한 글들인지 구별할 수 없음
  - related_name 작성

```python
class Article(models.Model):
    ...
    like_users = models.ManytoManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    ...
```

- 생성된 중개 테이블 : articles_article_like_users
- User - Article 간 사용 가능한 related manager
  - article.user - 게시글을 작성한 유저 - N:1
  - user.article_set - 유저가 작성한 게시글(역참조) - N:1
  - article.like_users - 게시글을 좋아요한 유저 - M:N
  - user.like_articles - 유저가 좋아요한 게시글(역참조) - M:N

```python
# like

path('<int:article_pk>/likes/', views.likes, name='likes')

def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```

```html
<form action="{% url 'articles:like' article.pk %}" method='POST'>
    {% csrf_token %}
    {% if request.user in article.like_users.all %}
    	<input type='submit' value='좋아요 취소'>
    {% else %}
    	<input type='submit' value='좋아요'>
    {% endif %}
</form>
```



## User-User

```python
class User(AbstractUser):
    # 재귀적 상황 - self
    # symmetrical=True : 1-2면 2-1이다
    followings = models.ManytoManyField('self', symmetrical=False, related_name='followers')
```

- `/accounts/<int:pk>/follow`/
- 팔로우 완료 후에는 `/accounts/<int:pk>/detail`/페이지로 리다이렉트

```python
from django.shortcuts import render, redirect, get_object_or_404

@ login_required
def follow(request, pk):
    # pk값의 유저을 로그인한 유저가
    # 팔로우 아닐시 팔로우
    # 팔로우일시 팔로우 취소
    # user = get_user_model().objects.get(pk=pk)
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        messages.warning(request, '스스로 팔로우 할 수 없습니다.')
        return redirect('accounts:detail', pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
   		user.followers.add(request.user)
    return redirect('accounts:detail', pk)
```

```html
{% if request.user in user.followers.all %}
<a href="{% url 'accounts:follow' user.pk %}">팔로우 취소</a>
{% else %}
<a href="{% url 'accounts:follow' user.pk %}">팔로우</a>
{% endif %}
```

- `article = get_object_or_404(Article, pk=pk)`
- `from django.views.decorator import require_POST`