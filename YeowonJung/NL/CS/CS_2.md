# 백엔드 CS - Spring, DB, Network

## Back-End
### Spring

- **Spring Framework**: Java 기반의 애플리케이션 개발을 위한 오픈소스 프레임워크. 
    - **Spring vs SpringBoot**: SpringBoot는 Spring을 더 쉽게 사용할 수 있게 해주는 도구. 복잡한 설정 없이 바로 개발을 시작할 수 있음.

- **MVC**: Model-View-Controller 디자인 패턴으로, Model이 애플리케이션의 데이터와 비즈니스 로직을, View가 사용자에게 보여지는 화면을, Controller가 사용자의 요청을 받아 Model과 View를 연결하는 역할을 담당.

- **DI(Dependency Injection)**: 의존성 주입. 객체가 필요로 하는 의존성을 외부에서 주입받는 방식. 스프링이 자동으로 객체를 생성하고 주입. 객체 간의 결합도를 낮추고 테스트가 용이해짐.

- **IoC(Inversion of Control)**: 제어의 역전. 객체의 생성과 관리를 개발자가 아닌 프레임워크가 담당. IoC의 구현체가 DI.

- **Bean**: 스프링 컨테이너가 관리하는 자바 객체. 어노테이션을 통해 등록하면 스프링이 객체의 생성과 의존 관계, 생명주기를 자동으로 관리.


### DB

- **Index**: 데이터베이스 테이블 검색 속도를 향상시키기 위한 자료 구조. 특정 컬럼에 대해 정렬된 상태를 유지. 검색 속도는 빨라지지만 데이터의 입력, 수정, 삭제는 느려질 수 있으며 추가 저장 공간이 필요.

- **Unique**: 특정 컬럼에 중복된 값이 들어가지 않도록 하는 제약조건.

- **SQL(Structured Query Language)**: 데이터베이스를 관리하고 데이터를 처리하기 위한 표준 프로그래밍 언어. 데이터의 삽입, 조회, 수정, 삭제 등의 작업 수행.

- **파티셔닝**, **샤딩**
    - **파티셔닝**: 큰 테이블이나 인덱스를 물리적으로 분할하는 기법. 행 기준으로 분할하는 수평 파티셔닝과 열 기준으로 분할하는 수직 파티셔닝이 있음. 하나의 데이터베이스 안에서 이루어짐.
    - **샤딩**: 데이터를 여러 개의 데이터베이스 서버로 분산하는 기법. 각각의 데이터베이스는 독립적으로 동작. 구현과 관리가 더 복잡하지만 부하 분산, 확장성에 좋음.

### Network

- **google.com 을 주소창에 입력하면 무슨일이 일어나는가?**: 
    1) DNS를 조회해서 도메인의 IP 주소를 찾고 
    2) TCP 연결과 HTTPS 보안 연결을 수립한 후 
    3) 구글 서버에 요청을 보내 
    4) 응답으로 받은 HTML, CSS, JavaScript를 통해 브라우저가 렌더링하여 
    5) 화면에 페이지를 표시.

- **HTTP**, **HTTPS**
    - **HTTP(HyperText Transfer Protocol)**: 웹 브라우저와 웹 서버가 데이터를 주고받기 위한 기본 프로토콜.
    - **HTTPS(HTTP Secure)**: HTTP에 보안 계층을 추가한 프로토콜. 데이터를 암호화하여 전송.

- **로드 밸런싱**: 여러 서버나 네트워크 장비에 트래픽을 분산시겨 시스템의 부하를 균등하게 분배하는 기술.

- **WS(Web Server)**, **WAS(Web Application Server)**
    - **WS**: 정적인 컨텐츠를 제공하는 서버. HTML, CSS, 이미지 등 변하지 않는 파일들을 브라우저에 전달.
    - **WAS**: 동적인 컨텐츠를 제공하는 서버. 사용자 요청에 따라 데이터를 처리하여 결과를 보여줌.