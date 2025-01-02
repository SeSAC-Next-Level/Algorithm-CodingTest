# Framework

- 개발을 위한 기본 구조
- 일정한 틀과 규칙을 가지고 무언가를 만들 수 있도록 하는 도구
- 정해진 규칙에 따라 비즈니스 로직 구현에 집중 할 수 있다

# Spring

- Java 기반의 프레임워크
- 웹 서비스를 만들기 위해 사용된다
- 웹 서비스를 구현하기 위한 라이브러리들이 제공된다
- 구현을 위한 설정을 직접 해야한다, 세밀한 제어(설정)가 가능하다
- WAS를 설치해야 한다

# Spring Boot

- Spring을 더 편하게 사용하기 위함
- 기본 설정을 제공하여 구현에 더 집중할 수 있다
- [[#Web Application Server|WAS]]가 내장되어 있다
- 어떤 설정이 되어 있는지 어떤 흐름으로 동작하는지 파악하기 어렵다

# Web Server VS Web Application Server

## Web Server

- 정적파일을 제공
- 정적 파일은 이미지, HTML, CSS, JS 변하지 않는 파일을 뜻한다.
- 동일한 데이터가 제공 됨

## Web Application Server

- 동적인 파일을 제공
- 프로그래밍 언어를 사용하여 웹 애플리케이션 실행
- 사용자의 요청에 맞는 데이터를 보여준다

# MVC

1. Model
	- 데이터와 비즈니스 로직을 담당
2. View
	- 사용자에게 데이터를 보여주는 UI 담당
3. Controller
	- 사용자 요청을 받아 처리하고 요청에 맞는 Model과 View를 연결

# 3 Tier Architechure

1. Presentation Layer
	- UI 처리
2. Business Logic Layer
	- 애플리케이션의 핵심 로직과 데이터 처리 담당
3. Data Access Layer
	- 데이터베이스와의 상호작용


| MVC Element | Spring MVC Component | 3 Tier Architechure        | Role                 |
| ----------- | -------------------- | -------------------------- | -------------------- |
| Controller  | Controller           | Presentation Layer         | 사용자 요청 처리 및 데이터 전달   |
| Model       | Service              | Business Logic Layer       | 비즈니스 로직 처리 및 트랜잭션 관리 |
| Model       | Repository           | Data Access ayer           | 데이터베이스와 상호작용         |
| View        | View                 | Presentation Layer(Output) | 사용자에게 데이터를 시각적으로 표시  |

# Bean

- [[#Spring Container|Spring Container]]에서 관리되는 객체
- 싱글톤으로 사용 됨
	- 하나의 인스턴스를 생성하여 사용하여 메모리를 절약 할 수 있음

# Spring Container

- Spring Bean의 생성, 관리, 제거를 [[#Inversion of Control|담당]]한다
- 로직에 필요한 객체를 [[#Dependency Injection|주입]]시켜준다
- 개발자는 별도의 생성 로직을 작성하지 않아도 된다
- 주입 과정이 눈으로 보이지 않아 흐름 파악이 어렵다

## Dependency Injection

- 의존성 주입
- 클래스에서 다른 클래스의 인스턴스를 소유할 때 이 인스턴스를 주입해주는 방법
1. 생성자 주입
2. 수정자 주입
3. 필드 주입
>하나의 애플리케이션에서 구현된 로직들이 변경되는 일은 자주 발생하지 않으므로 생성자 주입을 권장하고 있다.

## Inversion of Control

- 제어의 역전
- 프레임워크에게 객체관리, 의존성 주입을 위임하는 것

---

# Google.com을 주소창에 입력하면?
>https://www.google.com
1. DNS 서버에서 Google.com에 맞는 IP를 찾는다
2. IP 주소에 TCP 연결 요청
3. 데이터 암호화
4. 443 포트에 맞는 데이터
5. 랜더링

# HTTP vs HTTPS

## HTTP

- 기본 포트 80
- 서버/클라이언트 모델을 따라 데이터를 주고 받기 위한 프로토콜
- 요청 시 클라이언트의 정보들이 평문으로 전송됨

## HTTPS

- 기본포트 443
- HTTP로 전송되는 데이터를 암호화 함
- 대칭키, 비대칭키 활용
- 대칭키
	- 클라이언트, 서버 동일한 암복호화 키를 가짐
- 비대칭키
	- 클라이언트는 공개키
	- 서버는 비공개키를 가짐
	- 공개키로 암호화하여 비공개키로 복호화 진행

# Load Balance

- 서비스 간 트래픽을 분산한다.
	- 여러 서버로 요청을 분산
- 서버 앞 단에서 요청 부하는 줄여준다.
- 부하분산에 사용 됨

---

# Index

- 데이터 조회를 빠르게 할 수 있도록 한다
- 입력, 수정, 삭제는 상대적으로 느려진다
- 조회를 위해 정렬되는 추가공간이 필요하다

# Unique

- 컬럼의 값이 유일해야 하는 제약 조건
- unique index 생성 됨

# Transaction

- 여러 SQL을 하나의 작업 단위로 묶은 것

# 파티셔닝 vs 샤딩

| **항목**    | **파티셔닝**               | **샤딩**                    |
| --------- | ---------------------- | ------------------------- |
| **분할 범위** | 논리적 데이터 분할 (한 서버/DB 내) | 물리적 데이터 분할 (다수의 서버/DB 사용) |
| **분할 기준** | 범위, 리스트, 해시 등          | 주로 키(Hash) 기반             |
| **장점**    | 쿼리 최적화, 관리 효율성         | 확장성, 높은 처리량               |
| **단점**    | 동일 서버 리소스 제한           | 분산 트랜잭션 및 관리 복잡도          |
| **사용 목적** | 데이터 관리 및 성능 향상         | 확장성과 분산 시스템 구축            |