# Django5

## Django's Design Pattern

- 소프트웨어를 개발할 때 공통적인 설계 문제가 존재하며, 이를 해결할 때 자주 사용되는 구조와 해결책이 있음을 알게 됨
- 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나

- 디자인 패턴을 알고 있다면 서로 복잡한 커뮤니케이션이 매우 간단해짐

### MVC 소프트웨어 디자인 패턴

- 데이터 및 논리 제어를 구현하는 데 널리 사용되는 소프트웨어 디자인 패턴
- Model - View - Controller
  - Model - 데이터와 관련된 로직을 정리
  - View - 레이아웃과 화면을 처리
  - Controller - 명령을 model과 view 부분으로 연결

- MVC 소프트웨어 디자인 패턴의 목적
  - 관심사 분리
  - 더 나은 업무의 분리와 향상된 관리 제공
- Django는 MVC패턴을 기반으로 한 MTV(Model - Template - View) 패턴을 사용
  - Model - 데이터와 관련된 로직 관리, 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
  - Template - 화면상의 사용자 인터페이스 구조와 레이아웃 정의
  - View - Model & Template 중간 처리 및 응답 반환

### Database

- 스키마(Schema)
  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
- 테이블
  - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
  - 필드 : 속성, 컬럼
  - 레코드 : 튜플, 행
- PK(Primary Key)
- 쿼리(Query)

### Model

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

- `TextField()`
- `CharField()`
- 데이터베이스 스키마를 실제 데이터베이스에 반영하기 위한 과정이 필요

### Migration

```python
$ python manage.py makemigration
$ python manage.py migrate
```

## CRUD

