# Spring Framework

- Spring
  - Spring Frmework, Spring Boot 를 포함하는 생태계 전반을 포괄하는 용어
  - Spring Frmework + 관련 프로젝트 혹은 일부 모듈(Spring Security, Spring Data 등) = Spring
  - general 하게 사용하는 용어
- Spring Framework
  - Java EE 애플리케이션을 개발하기 위한 포괄적인 프레임워크
  - 모듈화된 구조로 구성 (AOP, Web 등 다양한 모듈)
  - IoC, DI 를 통해 객체 관리를 단순화
  - 트랜잭션 관리, 데이터 액세스, 보안 등 다양한 EE 기능 제공
  - 장점
    - 유연성 : 다양한 기술과 쉽게 통합 가능
    - 커뮤니티와 상태계 : 방대한 문서와 오픈소스 프로젝트
    - 표준화된 개발 방식 : EE 수준의 개발에 적합
  - 단점
    - 복잡할 설정과 구성
    - 러닝 커브가 높음
    - xml 설정
- Spring Boot
  - Spring Framework를 기반으로, 빠르고 간편하게 애플리케이션을 개발할 수 있도록 설계된 도구
  - **Convention over Configuration**(관습에 의한 설정)을 채택
  - 내장된 톰캣/제티 서버 제공
  - xml 설정 대신 주로 어노테이션과 프로퍼티 파일로 간단한 설정 가능
  - `spring-boot-starter-web` 으로 필요한 기능을 쉽게 추가
  - 내장 서버를 활용해 별도의 서버 구성 없이 애플리케이션 실행 가능
  - 설정이 단순해서 빠른 개발이 가능
  - 단점
    - 설정이 복잡하다고 느낄 수 있음
    - 내장 서버를 사용하는 경우 대규모 EE한계가 존재

## MVC

- Model View Controller 디자인 패턴
- Model
  - 애플리케이션의 데이터와 비즈니스 로직 담당
  - Service와 Repository가 Model에 해당
- View
  - 사용자에게 보여지는 화면을 담당
  - SSR방식의 경우 HTML, JSP, Thymeleaf
  - REST API를 사용할 경우 JSON 형태의 데이터
- Controller
  - 사용자의 요청을 받아 Model과 View를 연결하는 역할
  - 스프링에서는 @Controller @RestController 어노테이션 사용

## IoC (Inversion of Control 제어의 역전)

- 객체의 생성과 관리를 개발자가 아닌 프레임워크가 담당
- 기존에는 개발자가 직접 객체를 생성하고 관리했지만, 스프링에서는 스프링 컨테이너가 객체를 생성하고 관리
- IoC의 구현체가 DI

## DI (Dependency Injection 의존성 주입)

- 객체가 필요로 하는 의존성을 외부에서 주입받는 방식
- 의존성이란?
  - 한 클래스가 다른 클래스를 필요로 하는 것
  - 예를 들어 Service클래스는 Repository 클래스를 필요로 함
- 스프링의 경우 자동으로 객체를 생성하고 주입해줌
- DI장점
  - 컴포지션 방식보다 객체 간의 결합도는 낮춰줌
  - 테스트가 용이함
  - 코드의 재사용성이 높아짐

## Bean

- 스프링 컨테이너가 관리하는 자바 객체
- @ComponentScan @Component 어노테이션을 통해 빈으로 자동 등록 가능
- 자바 설정 파일에서 @Bean을 통해 수동 설정 가능

# DB

- Index
  - 자료의 정렬 상태를 유지하여 검색 속도를 높이는 장치
- Unique
  - 중복된 값을 가질 수 없는 특성
- SQL
  - 데이터베이스를 관리하고 처리하기 위해 사용하는 표준 프로그래밍 언어
- 샤딩
  - 큰 테이블을 동일한 스키마를 가진 여러 데이터베이스 서버에 shard 단위로 분산 저장하는 방법
  - 물리적으로 다른 서버에 저장하므로 트래픽 분산, 가용성 향상 장점이 존재함
  - 데이터 조회시 조인하는 어려움이 존재함
- 파티셔닝
  - 데이터베이스에서 테이블이나 인덱스를 작은 논리적 단위인 파티션으로 나누닌 것

# 네트워크

- [google.com](http://google.com) 을 주소창에 입력하면 무슨일이 일어나는가?
  - google.com의 IP주소를 찾기 위해 캐시에서 DNS 기록을 찾음
  - 캐시에 DNS기록이 없다면 DNS서버로 [google.com](http://google.com) IP 주소를 요청해서 받음
  - 웹 브라우저가 서버와의 TCP 연결을 시작
  - 연결이 되면 서버로 HTTP 요청을 전송
  - 웹 서버는 요청을 처리하고 브라우저로 응답
  - 웹 브라우저는 받은 응답을 렌더링
- HTTP/HTTPS
  - HTTP는 클라이언트아 서버 간에 데이터를 주고받는 데 사용되는 비보안 프로토콜
  - 텍스트 기반의 프로토콜로 HTML, CSS, JS와 같은 컨텐츠를 전송
  - 데이터를 암호화하지 않고 전송
  - stateless 상태 비유지 프로토콜로 통신이 끝나면 연결 상태를 유지하지 않음
  - 장점
    - 리소스가 적게 소모됨
  - 단점
    - 데이터가 암호화되지 않음
    - 민감한 정보 전송시 보안에 문제가 발생
- HTTPS
  - HTTP에 보안 기능(SSL/TLS)을 추가한 프로토콜
  - SSL/TLS를 통해 데이터가 암호화되어 전송
  - 인증서 사용 : 신뢰할 수 있는 기관(CA)이 발급한 인증서를 통해 서버 신뢰성 보장
- 로드 밸런싱
  - 클라이언트의 요청을 여러 서버로 고르게 분산시키는 작업
  - 사용하는 이유
    - 서버 과부하를 방지
- WS(Web Server) / WAS(Web Application Server)
  - WS
    - 클라이언트의 정적인 요청을 처리하는 서버
    - ex. tomcat
  - WAS
    - 클라이언트의 동적인 요청을 처리하는 서버
