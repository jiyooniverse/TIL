# Vue.js

- 프론트 프레임워크 : Vue.js, React, Angular
  - HTML, CSS, JavaScript를 활용해서 데이터를 볼수 있게 만들어줌

  - Vue.js : 사용자 인터페이스를 만들기 위한 진보적인 자바스크립트 프레임워크

    - SPA(Single Page Application) 지원 

      - 단일 페이지 애플리케이션으로 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 애플리케이션

      - 최초에만 페이지를 다운로드하고, 이후 동적으로 DOM구성

      - 동작 원리의 일부가 CSR(Client Side Rendering)의 구조를 따름

        > CSR : 서버에서 화면을 구성하는 SSR방식과 달리 클라이언트에서 화면을 구성
        >
        > - CSR과 SSR 비교
        >
        >   - CSR 
        >     - 장점 : 서버와 클라이언트 간 트래픽 감소, 사용자 경험 향상
        >     - 단점 : SSR에 비해 전체 페이지 렌더링 시점이 느림, SEO(검색 엔지 최적화)에 어려움이 있음
        >   - SSR
        >     - 장점 : 초기 구동 속도가 빠름, SEO에 적합
        >     - 단점 : 모든 요청마다 새로운 페이지를 구성하여 전달 
        >
        >   > SEO 대응 : 추가로 별도의 프레임워크 사용(Nuxt.js, Nextjs)

- MVVM Pattern : 애플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴

  - 구성 요소 : Model, View, View Model
  - Model : JavaScript의 Object 자료구조
  - View : DOM(HTML)으로 Data의 변화에 따라서 바뀌는 대상
  - ViewModel : Vue Instance로 View와 Model 사이에서 Data와 DOM 관리

