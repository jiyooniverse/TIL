# JavaScript

#### 1. JavaScript 필요성

- 브라우저 화면을 '동적'으로 만들기 위함
- 브라우저를 조작할 수 있는 유일한 언어 

> 브라우저(browser) : 웹 서버에서 이동하며 클라이언트와 서버 간 양방향으로 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어

#### 2. 브라우저에서 할 수 있는 일

- DOM 조작 : 문서(HTML) 조작
- BOM 조작 : navigator, screen, location, frames, history, XHR
- JavaScript Core(ECMAScript) : Data Structure(Object, Array), Conditional Expression, Iteration

> - DOM(Document Object Model) 이란? HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
>
> - BOM(Brower Object Model) 이란? 자바스크립트가 브라우저와 소통하기 위한 모델

#### 3. DOM 조작

1. 선택

   - querySelector(), querySelectorAll() : id, class 그리고 tag 선택자 등을 모두 사용 가능

     > - Live Collection : 문서가 바뀔 때 실시간으로 업데이트 됨
     >
     >   ex) HTMLCollection, NodeList
     >
     > - Static Collection(non-live) : DOM이 변경되어도 collection 내용에는 영향을 주지 않음. querySelectorAll()의 반환 NodeList만 static collection임.

2. 변경

   - createElement() : 작성한 태그명의 HTML 요소 생성하여 반환.
   - append(): 여러개의 Node 객체, DOMString을 추가 할 수 있음.
   - appendChild() : 한번에 오직 하나의 Node만 추가할 수 있음.

#### 4. Event

1. Event 개념 : 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체.
2. Event handler - addEventListener() : 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
3. Event 취소 - preventDefault() : 현재 이벤트의 기본 동작을 중단.(event.cancelable을 통해 취소 가능 여부 확인)