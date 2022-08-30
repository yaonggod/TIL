# CSS

## CSS 기본 스타일

### 크기 단위

- px (픽셀) - 고정적
- % - 가변적인 레이아웃에서 주로 사용
- em - 부모 요소에 대한 상속의 영향을 받음, 배수 단위
- rem - 상속의 영향을 받지 않음, 최상위 요소(html) 기준(16px)으로 배수 단위
- viewport : 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax

### 색상 단위

- 색상 키워드
- RGB 색상
- HSL 색상

 ### CSS 문서 표현

- 텍스트 : 서체(font-family), 서체 스타일(font-family, font-weight), 자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height) 등
- 컬러(color), 배경(background-image, background-color)

## CSS Selectors

- 기본 선택자

  - 전체 선택자
  - 요소 선택자 : HTML 태그를 직접 선택
  - 클래스 선택자 : .로 시작, 해당 클래스가 적용된 항목 선택
  - 아이디 선택자 : #로 시작, 해당 아이디가 적용된 항목 선택, 일반적으로 한 문서당 하나
  - 속성 선택자

- CSS 적용 우선순위

  1. 중요도 : 사용시 주의
     - !important

  2. 우선 순위 : 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
  3. CSS 파일 로딩 순서

- CSS 상속

  - 상속 되는 것 : Text 관련 요소(font, color, text_align), opacity, visibility 등
  - 상속 되지 않는 것 : Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등

  ```css
  <style>
  	p {
          /* 상속됨 */
          font-size: 15px;
          color: red;
          /* 상속 안됨 */
          border: 3px solid black;
    	}
  	span {
      
  	}
  </style>
  ```

  ```html
  <body>
      <p>안녕하세요 <span>테스트</span> 입니다.</p>
  </body>
  ```

## BOX model 

**CSS 원칙 1 : 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다**

- 하나의 박스는 네 부분으로 이루어짐

  - margin : 테두리 바깥의 외부 여백

    ```css
    .margin_1{
        /* 상우하좌 */
        margin: 10px;
    }
    .margin_2{
        /* 상하 좌우 */
        margin: 10px 20px;
    }
    .margin_3{
        /* 상 좌우 하 */
        margin: 10px 20px 30px;
    }
    .margin_4{
        /* 상 우 하 좌(시계방향) */
        margin: 10px 20px 30px 40px;
    }
    ```

  - border : 테두리

  - padding : 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용

  - content : 글이나 이미지 등 요소의 실제 내용

![boxmodel](C:\Users\이주용\Desktop\TIL\boxmodel.png)

- box-sizing
  - 기본적으로 모든 요소의 box-sizing은 padding을 제외한 content-box
  - 일반적으로 영역을 볼 때는 box-sizing을 border-box로 설정 가능

## CSS Display

**CSS 원칙 2 : display에 따라 크기와 배치가 달라진다.**

- `display : block`

  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  - div / ul, ol, li / p / hr / form

- `display : inline` 

  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지
  - width, height, margin-top, margin-bottom을 지정할 수 없다
  - 상하 여백은 line-height로 지정
  - span / a / img / input, label / b, em, i, strong

- `display : inline - block`

  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음

- `display : none`

  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility : hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않음

  