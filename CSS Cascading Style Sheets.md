# CSS: Cascading Style Sheets

CSS : HTML 문서의 요소가 화면, 종이, 음성이나 다른 매체 상에 어떻게 렌더링되어야 하는지 지정

1. CSS 파일 저장
2. head 태그 내에 <link href="styles/style.css" rel="stylesheet" type="text/css"> 붙여넣기
3. 브라우저 불러오기

## CSS의 ruleset

```css
p, li, h1 {
    color : red;
    width: 500px;
  	border: 1px solid black;
}
```

- 선택자(selector) : 꾸밀 HTML 요소 이름, 여러 요소를 선택할 수 있음
- 선언 : `color : red`와 같이 꾸미기 원하는 요소의 속성 명시
- 속성 : 주어진 HTML 요소를 꾸밀 수 있는 방법

- 속성 값 : 속성의 결과 중 하나

### 선택자의 여러 종류

```css
/* 요소 선택자 */
p {
    
}
/* 아이디 선택자 : 속성에 id="my_id"가 있는 경우*/
#my_id {
    
}
/* 클래스 선택자 : 속성에 class="my_class"가 있는 경우 */
.my_class {
    
}
/* 속성 선택자 */
img[src] {
    
}
/* 수도(Pseudo) 클래스 선택자 ex) a:hover - a 위에 마우스 포인터가 있을 때*/
a:hover {
    
}
```

### 글꼴과 문자

```css
/* 전체 문서 기본 설정 */
html {
    font_size : 10px;
    font_family : placeholder;
}
/* 개별 요소 설정 */
h1 {
  font-size: 60px;
  text-align: center;
}
p, li {
  font-size: 16px;
  line-height: 2;
  letter-spacing: 1px;
}
```

### 박스

- `padding` : 컨텐츠 주위의 공간
- `border`: padding 바깥쪽의 실선
- `margin`: 요소의 바깥쪽을 둘러싼 공간
- `width`: 너비
- `background-color`: 요소의 컨텐츠와 padding의 배경 색
- `color`
- `text_shadow`
- `display`

```css
html {
  background-color: #00539F;
}
body {
  width: 600px;
  margin: 0 auto; /* 상하는 0, 좌우는 auto */
  background-color: #FF9500;
  padding: 0 20px 20px 20px; /* 상 우 하 좌 (시계방향) */
  border: 5px solid black; /* 5px 두께의 실선 */
}
h1 {
  margin: 0;
  padding: 20px 0;
  color: #00539F;
  text-shadow: 3px 3px 1px black; /* 수평 수직 흐림 반경 그림자 색 */
}
img {
  display: block;
  margin: 0 auto; /* 가운데 정렬 */
}
```

