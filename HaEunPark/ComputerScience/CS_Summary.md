## FrontEnd

1. FrontEnd : 사용자에게 긍정적인 UX를 제공하는 UI를 개발하는 분야
2. UI & UX
	- UI (User Interface) : 사용자에게 보여지는 화면
	- UX (User Experience) : 사용자 경험
		- 이벤트 처리
		  사용자 입력(클릭, 키 입력 등)이나 애플리케이션 상태 변화에 따라 웹 페이지나 앱의 화면을 업데이트하거나, 관련 동작을 수행하는 과정
3. Semantic tag : 의미와 기능이 담긴 태그
	- <u>왜 Semantic tag가 필요할까?</u>
		- HTML 요소 자체가 의미를 지니고 있어 웹 페이지 구조를 명확하게 만들어줌.
		- 검색 엔진 최적화(SEO)
		- 웹 접근성 향상 
		  보조 기술이 웹 페이지를 해석하는 데 유용하게 작용함. 
		  EX. 시각 장애인이 텍스트 내용을 들을 수 있도록 돕는 TTS 기술
4. DOM (Document Object Model)
	- 웹문서를 객체(Object)모델로 표현하여, JavaScript를 사용해 웹 페이지의 요소에 동적으로 접근하고 조작할 수 있게 함. 
5. Tailwind & Bootstrap
	- Tailwind : 유틸리티 클래스 기반의 CSS 라이브러리
	- Bootstrap : UI 컴포넌트 기반의 CSS 프레임워크
6. SSR & CSR
	- SSR (Server Side Rendering)
	  서버에서 렌더링하고 완성된 HTML을 클라이언트에게 전달
		- 장점
			- 완성된 HTML을 전달하여 **초기 로딩 속도가 빠름**
			- 클라이언트가 서버로부터 완성된 HTML을 전달받아 검색 엔진이 제대로 콘텐츠를 크롤링하고 인덱싱할 수 있어 **SEO에 유리함**
		- 단점
			- 페이지 요청 시마다 서버에서 HTML을 렌더링해야 하므로 **서버 부하 증가**
			- 페이지마다 서버에 요청해야 하므로 **페이지 전환이 느림**
	- CSR (Client Side Rendering)
	  클라이언트(브라우저) 성능 발전으로 클라이언트 측에서 렌더링
		- 장점
			- 클라이언트에서 렌더링을 하여 **서버 부하 감소**
			- 한 번 로드된 후, 변화된 부분만 재렌더링 되어 **페이지 전환이 빠름** (새로운 데이터만 로드하여 화면 갱신)
		- 단점
			- JavaScript 파일을 실행하고 데이터를 가져와야 하므로 **초기 로딩 속도가 느림**
			- 데이터를 동적으로 로드하기 전, 빈 HTML을 먼저 받아 **SEO에 불리함**
7. SEO (Search Engine Optimization) : 검색 엔진 최적화
8. React
   JavaScript 라이브러리로 컴포넌트 기반의 UI를 구현하기 위해 사용
   Q. React를 사용하는 이유는?
   A. 코드의 컴포넌트화로 간편하고 빠른 개발과 유지 보수 가능
9. SPA (Single Page Application)
	- 페이지 이동 없이 사용자와의 상호작용에 따라 변화가 필요한 부분만 동적으로 업데이트함. 
	- 사용자의 요청에 따라 index.html 하나만 제공하면서, 상태 관리 대상인 값이 변화했을 때 그 값만 재렌더링하여 사용자에게 매끄러운 경험을 제공함.
10. Virtual DOM : 가상 돔
	- 기존에는 데이터 값이 바뀌면 전부 재렌더링했음.
	- 가상 돔이 상태 변화를 감지하여, 값이 바뀌면 실제 DOM과 값을 비교하고 바뀐 부분만 전달하여 재렌더링함.
	- 결국 실제 DOM에 대한 변화를 최소화하여 성능을 최적화함.
	- 장점
		- 비용 절감에 효과가 있음
		- 페이지 전환 속도가 빠름
		- 사용자 경험을 개선할 수 있음
		- 서버의 과부화를 줄임
11. Hook
	- 데이터의 상태를 관리하기 위해 사용함
	- 훅을 사용하지 않으면 화면에서 변동된 값이 적용되지 않음. 따라서 상태 관리를 위해 사용해야 함.
	  ex. useState, useEffect, useRef 등
12. 생명주기
    useEffect Hook을 사용하여 기능 처리
	- 마운트 : 컴포넌트가 처음 DOM에 추가될 때 실행
	- 업데이트 : 컴포넌트의 상태가 변경될 때 실행 (리렌더링)
	- 언마운트 : 컴포넌트가 DOM에서 제거될 때 실행
13. Node.js
    Chrome V8 JavaScript 엔진 위에 구축된, 서버 측에서 실행되는 JavaScript 환경 (브라우저 밖에서도 JavaScript를 사용하기 위함)
14. Next.js
    Q. Next.js의 도입 배경은?
    A. SEO 최적화가 어려운 React의 단점을 극복하기 위해,  첫 페이지는 SSR 방식으로 로딩하고 이후 페이지는 CSR 방식을 활용함.
15. Component : 재사용 가능한 UI 요소
	- HTML 파일을 코드화 시켜 코드의 반복성을 줄이고, 재사용성 높임
16. Props : 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달하는 매개변수
17. 비동기 (Asynchronous)
	- 코드가 실행되는 동안 다른 코드를 실행 (비동기적 처리)
	- 사용자가 요청을 보냈을 때, 응답을 기다리지 않고 다른 동작을 할 수 있음
	- 결국 코드 실행 순서를 제어하며, callback function, promise, async/await 등 다양한 방법으로 처리 가능함함
18. 비동기 통신 (Fetch & Axios)
    서버와 클라이언트 간 통신을 비동기적으로 하여, 응답을 기다리지 않고 다른 작업을 처리할 수 있음.
	- Fetch : 웹 브라우저가 기본적으로 제공하는 API
	- Axios : Promise 기반의 HTTP 클라이언트 라이브러리 
		- 장점
			-  서버와의 통신을 보다 편리하고 유연하게 처리 가능함
			- 인스턴스를 활용하여 baseURL을 지정할 수 있음
			- header에 필요한 정보들을 미리 넣어, 재사용 용이하게 함
19. Promise : 비동기 작업에 대해 성공과 실패를 처리하는 문법
	- 처리 순서를 정해 콜백 지옥을 방지함
20. Callback Function
    함수 안에 인자로 들어가는 함수
    - 매개변수 : 함수를 정의할 때 들어가는 parameter
    - 인자 : argument
21. 이벤트 루프 (Event Loop)
	- 비동기 통신 시 사용되며, call stack -> web API -> callback queue -> call stack 순으로 동작
	- 비동기 작업의 처리 순서: 
		1. 콜 스택에서 실행할 코드가 있으면 우선 실행 
		2. 비동기 작업이 끝나면 해당 콜백 함수가 콜백 큐에 들어감 
		3. 이벤트 루프는 마이크로태스크 큐(Microtask Queue)의 작업을 먼저 처리한 후, 콜백 큐에서 작업을 처리 
		4. `Promise`의 콜백은 마이크로태스크 큐에 들어가고, 콜백 큐보다 먼저 처리됨
	- callback queue 
		- task queue & micro task queue로 이루어지며, 더 중요한 정보를 다루는 micro task queue가 먼저 처리됨 (ex. Promise 객체)
22. URL (Uniform Resource Locator)
	- 인터넷에 있는 자원을 식별하는 주소
23. Interface (API)
	-  소프트웨어 어플리케이션이 서로 상호작용할 수 있도록 한 지점
	- HTTP 통신을 위한 지점 곧 URL
24. RESTful API
	- 데이터(resource)를 유추할 수 있고, HTTP method를 가지고 있음
	- HTTP method
		- GET, POST, PUT/PATCH, DELETE
25. HTTP : 서버와 클라이언트 간 데이터를 주고 받는 약속(통신 규약)
	- URL로 데이터를 요청하고 응답을 받음
	- 구성요소
		- header : 메타 데이터를 가짐
		- body : payload에서 확인 가능한 값을 가짐

## BackEnd

1. JVM
	- 자바 프로그램을 실행하기 위해 코드를 컴파일한 결과인 바이트코드를 OS 환경에 맞는 기계어로 변환하는 역할을 함
	- JRE : JVM + 라이브러리 (자바가 돌아가는 환경)
	- JDK : JRE + 개발자 도구 (컴파일러, TEST 도구, 디버거 등)
	- JVM의 메모리 구조
		- Heap : 기본 데이터 타입 외 모든 객체 (참조 객체)
			- GC (Garbage Collector)
			  heap에 있는 객체만 사용되지 않는 것 같으면 지우고 메모리 공간을 살림
		- Stack : 변수, 함수 등 실행 순서대로
		- Method : 상수, static method, 메소드
2. 객체 지향 프로그래밍 (Object Oriented Programming)
    - 작은 객체들을 구성하고 이들의 상호작용을 통해, 현실세계의 큰 문제를 해결하기 위한 프로그래밍 기법
    - 객체
      데이터와 그 데이터를 처리하는 메서드(함수)를 묶어서 하나의 단위로 만들어, 코드의 재사용성과 유지보수성을 높임
3. 객체 지향 프로그래밍의 4가지 특징
	- 캡슐화 (Encapsulation)
		- 외부에서의 접근을 막고 데이터를 은닉, 보호함
		- 접근제어자, 컴포지션
	- 상속 (Inheritance)
		- 부모 클래스의 공통적인 기능과 특징을 가진 자식 클래스도 접근 가능하다면 부모의 것을 사용할 수 있음
		- 부모 클래스를 자식 클래스가 확장하여 코드의 재사용성을 높이고, 일관성을 유지함
		- extends
	- 다형성 (Polymorphism)
		- 상위 타입으로 하위 타입 구현체를 생성할 수 있음 (동적바인딩)
		- 인터페이스, 메서드 오버라이딩
	- 추상화 (Abstraction)
		- 내부에 구현된 세부 사항은 숨기고, 외부에 필요한 핵심 기능만 노출함
		- 추상 클래스, 인터페이스
4. SOLID 원칙
	- Single Responsibility Principle (단일 책임 원칙)
		- 한 클래스는 하나의 책임만 가짐
	- Open-Closed Principle (개방-폐쇄 원칙)
		- 기존 코드를 변경하지 않고, 새로운 기능을 추가할 수 있어야 함 (확장 가능)
	- Liskov Substitution Principle (리스코프 치환 원칙)
		- 자식 클래스는 부모 클래스 객체를 완전히 대체할 수 있어야 함
	- Interface Segregation Principle (인터페이스 분리 원칙)
		- 큰 인터페이스를 작은 인터페이스로 분리해야 함 
	- Dependency Inversion Principle (의존성 역전 원칙)
		- 비즈니스 로직을 다루는 고수준 모듈은 세부적인 구현을 다루는 저수준 모듈을 알 필요가 없다.
		- 둘 다 추상화된 인터페이스에 의존해야 함.
5. Class & Interface
	- Class
	  비슷한 속성과 기능을 모아 새로운 타입을 정의할 수 있는 설계도
		- field : 속성
		- constructor : field의 값을 초기화하는 역할
		- method : 함수(기능)
	- Abstract Class 
	  자식 클래스가 구현해야 할 메서드를 정의하고, 일부 구현을 제공할 수 있는 클래스
	- Interface
	  필요한 기능을 반드시 구현하게끔 강제한 추상 메서드를 가진 클래스
		- 오버라이딩
		  자식 클래스에서 메서드를 구체화, 재정의 (추상 메서드 구)
		- 오버로딩
		  메서드 시그니처가 다르면 다른 함수로 정의됨
		  ex. 매개변수의 타입, 매개변수의 개수, 메서드 이름
6. 접근제어자 (Access Modifier)
	- public : 전체 공개
	- default : 같은 패키지 내에서만 접근 가능
	- protected : 같은 패키지 + 다른 패키지의 자식 클래스
	- private : 같은 클래스에서만 접근 가능