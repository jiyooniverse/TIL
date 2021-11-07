# ECMAScript6

### 변수와 식별자

- let, const, var

|       | 재선언 | 재할당 |   스코프    |
| :---: | :----: | :----: | :---------: |
|  let  |   X    |   O    | 블록 스코프 |
| const |   X    |   X    | 블록 스코프 |
|  var  |   O    |   O    | 함수 스코프 |



### 타입과 연산자

- 원시 타입 : number, string, boolean
- 참조 타입: objects > array, function, ...



### 조건&반복

- 조건
  - if : 조건 표현식의 결과값을 Boolean타입으로 변환 후 참/거짓 판단
  - switch : 조건 표현식의 결과값이 어느 값에 해당하는 지 판별 
- 반복문
  - while : 조건문이 참인 동안 반복
  - for : for (`initailization`; `condition`; `expression`)
  - for ... in : 객체의 속성 순회
  - for ... of : 반복 가능한 객체(Array, Map, Set, String, ...) 순회화며 값을 꺼낼 때 사용

### 함수

참조 타입 중 하나로 function 타입에 속한다.

- 함수 정의
  - 함수 선언식 

    익명함수 불가능, 호이스팅 O

    ```javascript
    function name(args) {
        // do something
    }
    ```

  - 함수 표현식

    익명함수 가능, 호이스팅 X

    ```javascript
    [const myFunction = ] function (args) {
        // do something
    }
    ```

- 화살표 함수 

  - function 키워드 생략 가능
  - 매개변수가 하나라면 '()'도 생략 가능
  - 표현식이 하나라면 '{}'과 return 생략 가능

- JavaScript의 함수는 **일급 객체**에 해당한다.
  - 일급 객체
    - 변수에 할당 가능
    - 함수의 매개 변수로 전달 가능
    - 함수의 반환 값으로 사용 가능



### 자료구조

- Array : 키와 속성들을 담고 있는 참조 타입의 객체

  - array.reverse() : 순서 반대로 정렬
  - array.push(`value`) : 배열 가장 뒤에 요소 추가
  - array.pop() : 배열의 마지막 요소 제거
  -  array.unshift(`value`) : 배열의 가장 앞에 요소 추가
  - array.shift() : 배열의 첫번째 요소 제거
  - array.includes(`value`) : 배열의 특정 값이 존재하는 지 판별 후 참 또는 거짓 반환
  - array.join(`[separator]`) : 배열의 모든 요소 연결하여 반환(구분자 생략 시 쉼표 기본 값으로 적용)
  - array.forEach((element[, index, array]) => { // do something}) : 반환 값이 없는 메서드
  - array.map((element[,index, array]) => {// do something}) : 콜백 함수의 반환값을 요소로 하는 새로운 배열 반환
  - array.filter((element[,index, array]) => { //do something}) : 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환
  - array.reduce((acc, element, [index, array]) => { // do something}, initialValue) : 반환값을 acc에 누적 후 반환, initialValue가  acc의 초기값이며 없을 경우, 배열의 첫 번째 값
  - array.find((element[,index, array]) => { // do something }) : 반환 값이 참이면 해당 요소를 반환
  - array.some((element[,index, array]) => { // do something }) : 배열의 요소 중 하나라도 주어진 판별 함수를 통과 하면 참을 반환
  - array.every((element[,index, array]) => { // do something }) : 배열의 모든 요소가 주어진 판별 함수를 통과 하면 참을 반환

- Object : 속성의 집합으로 중괄호 내부에 key와 value의 쌍으로 표현. key는 문자열 타입만 가능. value는 모든 타입 가능.

  - 속성명 축약

    - key와 할당하는 변수 이름이 같으면 축약 가능

      ```javascript
      const book = {
          title,	// title: title
          cost,	// cost: cost
      }
      ```

    - 매서드명 축약

      ```javascript
      const newObj = {
          // old version
          // greeting: function () {}
          greeting() {
              console.log('Hi!')
          }
      };
      
      newObj.greeting()
      ```

    - 계산된 속성 : key이름을 표현식을 통해 동적으로 생성 가능

      ```javascript
      const key = 'keyName'
      const value = ['a', 'b', 'c', 'd']
      
      const test = {
          [key]: value,
      }
      ```

    - 구조 분해 할당 : 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당 할 수 있음

      ```javascript
      const {name, userId, phoneNumber} = userInformation
      ```

  - JSON(JavaScript Object Notation)

    - key-value쌍의 형태로 데이터 표기하는 언어 독립적 표준 포맷
    - 문자열 타입으로 구문 분석(parsing)이 필수
    - 자바스크립 내 JSON 조작 내장 메서드
      - JSON.parse() : Json => 자바스크립트 객체
      - JSON.stringfy() : 자바스크립트 객체 => Json