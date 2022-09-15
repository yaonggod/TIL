# JavaScript

## JavaScript Intro

- 브라우저 : URL로 웹(WWW)을 탐색하여 서버와 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어
  - Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safari

- JavaScript의 필요성
  - 브라우저 화면을 '동적'으로 만들기 위함
  - 브라우저를 조작할 수 있는 유일한 언어

## DOM(Document Object Model)

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 문서가 구조화되어 있으며 각 요소는 객체로 취급
- 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - window : DOM을 표현하는 창, 가장 최상위 객체(작성 시 생략 가능)
  - document : 페이지 컨텐츠의 Entry Point 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함
  - navigator, location, history, screen
- 파싱(Parsing)
  - 구문 분석, 해석
  - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

## BOM(Browser Object Model)

- 자바스크립트가 브라우저와 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
- window 객체는 모든 브라우저로부터 지원받으며 브라우저의  창(window)을 지칭

## JavaScript Core(ECMAScript)

- 브라우저(BOM)과 그 내부의 문서(DOM)를 조작하기 위해 JS를 학습

## DOM 조작

- 순서 : 1. 선택 2. 변경

### 선택

- `document.querySelector(selector)`
  - 제공한 선택자와 일치하는 element 하나 선택
  - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)
- `document.querySelectorAll(selector)`
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  - 지정된 셀렉터에 일치하는 NodeList를 반환
- `getElementById(id)` - 단일 element 반환
- `getElementsByTagName(name)` - HTMLCollection 반환
- `getElementsByClassName(names)` - HTMLCollection 반환
- HTMLCollection & NodeList
  - HTMLCollection - name, id, index 속성으로 각 항목에 접근 가능
  - NodeList - index로만 각 항목에 접근 가능, forEach메서드 및 다양한 메서드 사용 가능
  - 둘 다 LiveCollection이지만, `querySelectorAll()`에 의해 반환되는 NodeList는 StaticCollection임
- Collection
  - Live Collection - 문서가 바뀔 때 실시간으로 업데이트
  - Static Collection - DOM이 변경되어도 collection의 내용에 영향을 주지 않음

### 변경

- `document.createElement()`
  - 작성된 태그 명의 HTML 요소를 생성하여 반환
- `Element.append()`
  - 특정 부모 Node의 자식 NodeList중 마지막 자식 다음에 Node객체나 DOMString을 삽입
  - 여러 개 추가 가능, 반환값 없음
- `Node.appendChild()`
  - Node객체만 추가 가능, 한번에 하나만 추가 가능
  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
  - 추가된 Node 객체 반환

- `Node.innerText`
  - Node객체와 그 자신의 텍스트 컨텐츠(DOMString)을 표현
  - 즉 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
- `Element.innerHTML`
  - 요소 내에 포합된 HTML 마크업을 반환
  - 참고 : XSS 공격에 취약하므로 사용 시 주의

### 삭제

- `ChildNode.remove()` : Node가 속한 트리에서 해당 Node를 제거
- `Node.removeChild()` : DOM에서 자식 Node를 제거하고 제거된 Node를 반환

### 속성

- `Element.setAttribute(name, value)`
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
- `Element.getAttribute(attributeName)`
  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자는 값을 얻고자 하는 속성의 이름