# HTML : Hypertext Markup Language

## HTML 기본

HTML : 웹 페이지와 그 내용을 구조화하기 위해 사용하는 코드, 컨텐츠에서 여러 개의 다른 부분들을 구별하기 위해 하는 여러 요소들로 구성되어 있음

```html
<!-- 독립적인 문단임을 명시하기 위해 p태그로 둘러쌈 -->
<p> <!-- 여는 태그 -->
    내 고양이는 고약해! <!-- 컨텐츠 -->
</p> <!-- 닫는 태그 -->
```

### HTML 요소

1. 여는 태그
2. 닫는 태그
3. 컨텐츠

### 속성

실제 콘텐츠로 표시되길 원하지 않는 요소의 추가적인 정보

1. 요소 이름과 속성 사이에 공백이 있어야 함
2. 속성 이름 뒤에 등호(=)가 와야 함
3. 속성 값의 앞뒤에 ''나 ""가 있어야 함

```html
<p class='fxxking cat'>내 고양이는 고약해!</p>
```

### 요소 중첩(nesting)

```html
<p class='fxxking cat'>내 고양이는 <strong>존나</strong> 고약해!</p>
```

### 빈 요소

```html
<img src='이미지 경로' alt='이미지를 볼 수 없는 경우 대체할 텍스트'>
```

### HTML 문서 해부

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

`<!DOCTYPE html>`: html로 인정받기 위한 일종의 규칙

`<html></html>`: html 페이지 전체의 컨텐츠를 감싸는 root 요소

`<head></head>`: html 페이지에서 보여지지 않는 부분의 컨테이너 역할. 페이지 설명, CSS, 문자 집합 선언 등

`<body></body>`: html 페이지에서 보이는 부분의 모든 컨텐츠

`<meta charset="utf-8">`: 문서가 사용할 문자 집합을 utf-8(대부분의 문자를 나타낼 수 있음)로 설정

`<title></title>`: 페이지가 로드되는 브라우저의 탭에 표시될 제목 요소

### 이미지

```html
<img src='이미지 경로' alt='이미지를 볼 수 없는 경우 대체할 텍스트'>
```

### 제목

```html
<h1>제목1</h1>
<h2>제목2</h2>
<h3>제목3</h3>
<h4>제목4</h4>
<h5>제목5</h5>
<h6>제목6</h6>
```

### 문단

```html
<p>내 고양이는 고약해!</p>
```

### 목록

```html
<!-- 순서 없음 -->
<ul>
    <li>고양이</li>
    <li>강아지</li>
    <li>앵무새</li>
</ul>

<!-- 순서 있음 -->
<ol>
    <li>세수하기</li>
    <li>양치하기</li>
    <li>자기</li>
</ol>
```

### 연결

```html
<a href="https://www.naver.com">네이버로 가기</a>
```



