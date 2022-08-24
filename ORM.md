# ORM

- Object Relational Mapping

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술

- 파이썬에는 SQLAlchemy, peewee 등 라이브러리가 있으며 Django에서는 내장 Django ORM을 활용

- 모델 설계 및 반영

  1. 클래스를 생성하여 내가 원하는 DB의 구조를 만든다

     ```python
     from django.db import models
     
     class Genre(models.Model):
         name = models.CharField(max_length = 30)
     ```

  2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일 생성

     ```python
     $ python manage.py makemigrations
     ```

  3. DB에 migrate함

     ```python
     $ python manage.py migrate
     ```

  - Migration(마이그레이션)
    - model에 생긴 변화를 DB에 반영하기 위한 방법
    - 마이그레이션 파일을 만들어 DB 스키마를 반영

## ORM 기본 조작

- Create

  ```python
  Genre.objects.create(name = '발라드')
  
  genre = Genre()
  genre.name = '락'
  genre.save()
  ```

- Read

  ```python
  # 1. 전체 데이터 조회
  Genre.objects.all()
  
  # 2. 일부 데이터 조회(get)
  Genre.objects.get(id = 1)
  
  # 3. 일부 데이터 조회(filter)
  Genre.objects.filter(id = 1)
  
  # get과 filter의 차이 : get은 해당하는 유일한 값을 리턴, filter는 조건에 맞는 값들을 일종의 리스트(QuerySet)으로 리턴
  ```

- Update

  ```python
  genre = Genre.objects.get(id = 1)
  genre.name = '트로트'
  genre.save()
  ```

- Delete

  ```python
  genre = Genre.objects.get(id = 1)
  genre.delete()
  ```

  