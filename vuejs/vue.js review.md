# vue.js review

### 1. Intro 

1. **Single Page Application**: 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 어플리케이션

   - 동작 원리의 일부가 CSR의 구조를 따름

     > CSR(client side rendering)
     >
     > - 서버에서 화면을 구성하는 SSR 방식과 달리 클라이언트에서 화면을 구성
     >
     > - 장점 
     >
     >   - 서버와 클라이언트 간 트래픽 감소	
     >   - 사용자 경험 향상
     >
     > - 단점 
     >
     >   - SSR에 비해 전체 페이지 렌더링 시점이 느림
     >
     >   - SEO(검색 엔진 최적화)에 어려움이 있음 
     >
     >     (하지만 SEO대응 기술 존재, Nuxt.js)

   - MVVM Pattern : 애플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴

     - Model : JavaScript Object 자료 구조로 Vue Instance 내부 data로 사용

     - View : DOM(HTML)으로 Data의 변화에 따라서 바뀌는 대상
     - View Model : Vue Instance로 View와 Model사이에서 Data와 DOM에 관련된 모든 일을 처리

2. Syntax of Vue.js

   - Options/Dom - `el` : Vue 인스턴스에 연결할 기존 DOM 엘리먼트

   - Options/Data - `data` : Vue 인스턴스 데이터 객체

     > 주의: 화살표 함수 사용 x

   - Options/Data - `methods` : Vue 인스턴스에 추가할 메서드

   - Options/Data -`computed` : 계산된 속성. 종속된 데이터가 변경될 때만 함수를 실행. 반드시 반환값 필요. (선언형 프로그래밍)

   - Options/Data-`watch`: 데이터 감시하다 변화가 일어났을 때 실행되는 함수.(명령형 프로그래밍)

   - Options/Assets-`filter`: 텍스트 형식화를 적용할 수 있는 필터

     ```html
     <div id="app"> </div>
     ```

     ```javascript
     const app = new Vue({
     	el: '#app',
     	data: {
     		message: 'Hello',
             num: 2,
     	},
         methods: {
             greeting: fucntion () {
             console.log('hello')
         	}
         },
         computed: {
              doubleNum: function () {
         		return this.num *2
     		 }
     	},
         watch: {
             num: function () {
                 console.log(`${this.num}이 변경되었습니다.`)
             }
         },
         filters: {
             getOddNums: function (nums) {
                 const oddNums = nums.filter(function (num) {
                   return num % 2                                      
                 })
                 return oddNums
             }
         }
     })
     ```

   - Interpolation(보간법)

     - Text  : {{ msg }}
     - Attributes: <div :id="dynamicId">

   - Template Syntax

     - v-show와 v-if

       v-show는 display속성을 hidden으로 만들어 토글. 실제로 렌더링은 되지만 눈에서 보이지 않음. 

       v-if는 전달인자가 false인 경우 렌더링 되지 않음.

     - `v-on`  :엘리먼트에 이벤트 리스너 연결. 약어 @

       > v-on:click => @click

     - `v-bind`: html요소 속성에 vue 데이터 값 할당. 약어 :

       > v-bind: href => :href

     - `v-model`: html form 요소의 값과 data를 양방향 바인딩

   - Lifecyle Hooks

     - created : vue 인스턴스가 생성된 후에 호출 됨

### 2. SFC, router

1. SFC(single file components)

   - Vue 컴포넌트 기반 개발의 핵심 특징
   - 하나의 컴포넌트는 .vue 확장자를 가진 하나의 파일 안에서 작성되는 결과물

2. Vue CLI

   - Vue CLI : Vue.js 개발을 위한 표준 도구
   - `Node.js` : 자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경
   - `NPM`(Node Package Manage) : 자바스크립트 언어를 위한 패키지 관리자
   - `Babel` : 자바스크립트의 ECMA6 코드를 이전 버전으로 번역/변환해 주는 도구
   - `Webpack` : 모듈간 의존성 문제를 해결하기 위한 도구

3. Pass Props & Emit Events

   > 부모는 자식에게 데이터를 전달(Pass props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)

   - 컴포넌트 등록 3단계 

     ```vue
     <template>
     	<div>
             <!-- 3. 보여주기 -->
             <about 
                my-message="This is prop data"
                :parent-data="parentData"
              />
         </div>
     </template>
     
     <script>
     // 1. 불러오기
     import About from './components/About.vue'
     
     export default {
         name: 'App',
         data: function () {
             return {            
                 parentData: 'This is parent Data',
             }
         },
         components: {
             // 2. 등록하기
             About
         }
     }
     </script>
     ```

   - `About.vue`

     ```vue
     <script>
     export default {
         name: 'About',
         // props 선언
         props: {
             myMessage: String,
     		parentData: String,
         }
     }
     </script>
     ```

   > Props 시 숫자 전달하려고 할 때, v-bind 사용하기

   - Emit event 작성

     > **현재 인스턴스**
     >
     > this.$emit('child-input-change', this.childInputData)
     >
     > **부모 인스턴스**
     >
     > <about @child-input-change="parentGetChange"/>

4. Vue Router

   - route에 컴포넌트를 매핑한 후, 어떤 주소에서 렌더링할 지 알려줌

   - SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공

   - `router-link` : 사용자 네이게이션을 가능하게 하는 컴포넌트

   - `router-view`: 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트

   - History mode : HTML History API를 사용해서 router구현

   - 프로그래밍 방식 네비게이션

     > router.push('home')
     >
     > router.push({name: 'Home'})

     - 동적 인자 전달

       > path : /user/:userName

       > html => {{$route.params.userName}}
       >
       > js => this.$route.params.userName

       > <router-link :to="{ name: 'Home', params: {userName: 'John'}}"/>

### 3. Vuex

"상태 관리 패턴 + 라이브러리 "로 애플리케이션의 모든 컴포넌트에 대한` 중앙 집중식 저장소` 역할

1. Vuex 핵심 컨셉

   >  Vue Components(dispatch) => Actions(commit) -> Mutations -> State

   - `State` : 중앙에서 관리하는 모든 상태 정보(data)
   - `Mutations`  :실제로 state를 변경하는 유일한 방법
   - `Actions` :context객체 인자를 받음. 
   - `Getters`: state를 변경하지 않고 활용하여 계산을 수행(computed 속성과 유사)

2. Component Binding Helper

   - mapState, mapGetters, mapActions, mapMutations

     > this.$store.state.todos 
     >
     > =>
     >
     > import {mapState} from 'vuex'
     >
     > ...mapState(['todos', ])

     mapActions 사용 시 payload는 template에서 함수 인자로 넘겨줌

