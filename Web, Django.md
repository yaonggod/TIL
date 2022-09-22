# Web, Django 

## 프레임워크

- 웹 서비스 개발에 필요한 것 : 로그인, 로그아웃, 회원관리, 데이터베이스, 서버, 클라이언트, 보안 등
- 이 기술들을 직접 만들 필요는 없고, 잘 만들어진 것들을 가져다가 좋은 환경에서 잘 쓰면 됨
- 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것이 **프레임워크**임
- 프레임워크를 잘 사용하면 내가 만들고자 하는 본질에 집중해 개발할 수 있음
- Django - 2020 Github Star 수 기준 2위 프레임워크, 다양한 서비스에거 검증됨

## Web

- WWW(World Wide Web) - 전 세계에 퍼져있는 거미줄 같은 연결망

## 클라이언트-서버

- 클라이언트
  - 웹 사용자의 인터넷에 연결된 장치
  - 웹 브라우저
  - 서비스를 요청하는 주체
- 서버
  - 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
  - 클라이언트가 웹 페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
  - 요청한 서비스를 응답하는 주체
- 예시 - Google 접속하기
  - **(클라이언트)**인터넷에 연결된 구글 컴퓨터에게 Google 홈페이지.html 파일을 요청 -> **(서버)**구글 컴퓨터가 Google 홈페이지.html 파일을 인터넷을 통해서 우리 컴퓨터에 응답 -> 받은 파일을 웹 브라우저가 우리가 볼 수 있는 형태로 해석

## Web browser, Web page

- 웹  브라우저
  - 웹에서 페이지를 찾아 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
  - 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는(렌더링) 프로그램

- 웹 페이지
  - 정적 웹 페이지(static web page)
    - 있는 그대로를 제공
    - 한 번 작성한 html파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 페이지
  - 동적 웹 페이지(dynamic web page)
    - 사용자의 요청에 따라 서버가 내용을 수정하여 클라이언트에게 전달되는 페이지
    - 다양한 서버 사이드 프로그래밍 언어(python, java, c++) 사용 가능 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

## Django 구조 이해하기 (MTV Design Pattern)

- Software Design Pattern : 자주 사용되는 소프트웨어의 구조를 일반적으로 구조화한 것
  - 클라이언트-서버 구조도 소프트웨어 디자인 중 하나

- MVC 소프트웨어 디자인 패턴 : Model - View - Controller
  - Model : 데이터와 관련된 로직을 관리
  - View : 레이아웃과 화면, 인터페이스 구조 처리
  - Controller : 명령을 model과 view부분으로 연결
  - 목적 : 관심사 분리 - 각 부분을 독립적으로 개발하여 효율적인 개발과 유지보수가 가능
- Django는 MVC 패턴을 기반으로 한 MTV(Model - Template - View) 패턴을 사용, MVC랑 비슷

## Django Quick Start

- 가상 환경

  ```bash
  $ python -m venv 가상환경이름
  # 활성화
  $ source 가상환경이름/Scripts/activate
  # 비활성화
  $ deactivate
  ```

- Django 3.2(LTS) 버전 설치

  - LTS(Long Term Support) - 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어 버전
  - 프로젝트명에는 python이나 django에서 사용중인 키워드 및 - 사용 불가
  - .을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성하게 됨
  - 서버는 ctrl + c로 끄면 됨
  - 서버 실행 후 localhost:8000으로 들어가서 메인 페이지 확인

  ```bash
  $ pip install django==3.2.13
  $ pip list
  
  # 프로젝트 생성
  $ django-admin startproject 프로젝트명 .
  # 프로젝트 폴더로 진입
  $ cd 프로젝트명
  # 서버 실행
  $ python manage.py runserver
  # 애플리케이션 생성 - 애플리케이션명은 복수형으로 작성 권장
  $ python manage.py startapp 애플리케이션명
  ```

- 프로젝트 구조
  - init.py
    - python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시
  - asgi.py
    - django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용
  - settings.py
    - django 프로젝트 설정을 관리
  - urls.py
    - 사이트의 url과 적절한 views의 연결을 지정
  - wsgi.py
    - web server gateway interface
    - django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용
  - manage.py
    - django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티
- Django Application
  - admin.py - 관리자용 페이지 설정
  - apps.py - 앱의 정보
  - models.py - 애플리케이션에서 사용하는 Model 정의
  - tests.py - 프로젝트의 테스트 코드 작성
  - views.py - view함수 정의
  - 프로젝트에서 앱을 사용하기 위해서는 settings.py에 INSTALLED_APPS에 앱 반드시 추가

- 프로젝트, 앱
  - 프로젝트는 앱의 집합, 앱은 여러 프로젝트에 있을 수 있음
  - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할 담당, 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장