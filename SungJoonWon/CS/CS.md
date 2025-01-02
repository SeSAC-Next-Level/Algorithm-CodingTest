- Front-End

  - 생명주기

  - component
  - SPA

  - SSR, CSR

  - 비동기

    사용자가 요청 했을 때에 결과를 기다리지 않고 다른 거서을 요청할수있다

  - 비동기 통신
    응답을 기다리지않고 비동기 통신

  - http = 서버와 클라이언트간의 통신 약속을 정해주는것 url을 통해 됨
  - 클라리언트와 서버사이에서 약속된 규약
  - header 와 body 로 이루어져 있으며
  - header은 메타 데이터로 이루어져있음

  - axios는 baseURL과 emv로 따로 저장가능
  - nextJS는 첫 페이지를 SSR로 줄수있음, 검색, 크롤링에 용이함

  - 리액트의 장점
  - 상태변화를 할떄 변화할 위치만 제 렌더링 함으로 사용자경험이 좋음.
  - 상태변화가 되면 버츄얼 돔이 변경됨
  - 컴포넌트로 구성되있음
  - props = 부모컴포넌트에서 자식 컴포넌트로 데이터를 주는것

  - 훅 데이터의 상태를 관리할떄 쓰는것
  - 훅을 통해서 값을 바꾸지않으면 화면에 적용되지않음.

- 버츄얼돔
  기존에는 전체가 전부 렌더링됨

  사용자 클라이언트 메모리에 저장됨 그래서 필요한 부분만 렌더링이가능
  속도빠름
  비용절감

- 시맨틱태그
- 의미, 기능이 있는 태그이며 시각장애인을 위해 각각의 TTS에서 각각의 태그를 알아봄

- 이벤트 루프
- webApi - collBackQ - collstack
- 끝나고 오는값이 프라미스
  프라미스 - 비동기 작업에 대해 성공과 실패를 확인하는 것
  콜백 지옥이 방지됨

nodeJS DOM 조작이 안되는이유
크롬의 v8엔진은 javascript만 사용가능하게 만들었으며
v8엔진을 똑! 때와서 만들었기때문에 javascript만 사용가능

restfull Api
리소스가 있으며(api명 만으로 어떤 기능인지 유추가 가능)
method가 정확한 api(get, post, put, path)

인터페이스
http통신을 위한 지점

- class
  특정 개념이나 대상에 대해서 개발에 필요한 특징들을 추출하기 위한
  위한 설계도

클래스들이 모여 하나의 문제를 해결하기위한것이 oop(객체지향)

인터페이스 클레스에서 만들어야 하도록 만들어주는 추상 메서드

다형성 - 동적 바인딩, 인터페이스, 오버라이딩
상속 - 중복을 줄일 수 있다 부모클래스의 모든 것들을 자식클래스가 사용할수있다. 코드 재사용이 용이하고 반복을 줄임
캡슐화 - 접근제어자와 컴포지션을 통해 만족시킴
추상화 - 구체적인 내부 로직인지 알지 못해도 외부에서 사용될 수 있다

JVM - 컴파일된 바이트 코드를 현재 실행되고 있는 os환경마다 기계어로 만들어줌

---

### **Spring Framework**

- **Spring Framework**는 자바 기반의 애플리케이션 개발을 지원하는 오픈소스 프레임워크로, 객체 지향 프로그래밍의 원칙과 설계 패턴을 따릅니다.
- 핵심 개념:
  - **IoC (Inversion of Control)**: 객체 생성과 관리를 컨테이너(Spring 컨테이너)가 담당하여 개발자는 비즈니스 로직에 집중할 수 있음.
  - **DI (Dependency Injection)**: 객체 간의 의존성을 주입받아 코드의 결합도를 낮추고 테스트를 용이하게 함.
  - **AOP (Aspect-Oriented Programming)**: 공통적으로 사용되는 로직(예: 로깅, 보안)을 애플리케이션의 핵심 로직에서 분리.

---

### **Spring Boot**

- **Spring Boot**는 Spring Framework의 설정 복잡성을 줄이고 빠른 애플리케이션 개발을 돕는 프레임워크입니다.
- 특징:
  - **자동 설정(Auto Configuration)**: 애플리케이션의 설정을 자동으로 처리.
  - **내장 웹 서버**: Tomcat, Jetty, Undertow와 같은 서버를 포함.
  - **간단한 프로젝트 초기화**: Spring Initializr로 빠른 프로젝트 생성 가능.
  - Spring Boot는 Spring Framework의 확장으로, 더 많은 편의성을 제공합니다.

---

### **Spring vs Spring Boot**

| **Spring Framework**            | **Spring Boot**                                   |
| ------------------------------- | ------------------------------------------------- |
| 설정이 복잡하고 수동으로 처리   | 자동 설정과 내장 서버로 더 간단하게 개발 가능     |
| 직접 XML 또는 Java Config 사용  | Auto Configuration으로 설정 부담 감소             |
| 의존성 관리가 상대적으로 어려움 | Starters(예: `spring-boot-starter`)로 의존성 관리 |

---

### **MVC (Model-View-Controller)**

- Spring MVC는 웹 애플리케이션에서 사용하는 아키텍처 패턴입니다.
- 구조:
  - **Model**: 데이터를 표현하며 비즈니스 로직과 관련.
  - **View**: 데이터를 사용자에게 보여주는 역할(HTML, JSON, XML).
  - **Controller**: 사용자 요청을 처리하고 적절한 Model과 View로 연결.
- Spring MVC에서는 `@Controller`와 `@RestController` 어노테이션을 사용해 컨트롤러를 정의합니다.

---

### **DI (Dependency Injection)**

- 객체 간 의존성을 외부에서 주입받는 방식으로, 코드 결합도를 낮추고 유연성을 높입니다.
- Spring에서는 `@Autowired`, 생성자 주입, Setter 주입 방식으로 DI를 구현합니다.

---

### **IoC (Inversion of Control)**

- 객체의 생성, 초기화, 생명 주기 관리를 개발자가 아닌 컨테이너(Spring IoC Container)가 제어.
- Spring은 IoC 컨테이너를 통해 DI를 지원하며, Bean으로 관리되는 객체를 주입합니다.

---

### **Bean**

- Spring IoC 컨테이너에서 관리되는 객체를 **Bean**이라고 합니다.
- Bean 정의:
  - **Java Config**: `@Bean` 어노테이션으로 등록.
  - **Component Scan**: `@Component`, `@Service`, `@Repository` 어노테이션.
- Bean 생명주기: 객체 생성 → 의존성 주입 → 초기화 → 소멸.

---

### **JPA (Java Persistence API)**

- Java 표준 ORM(Object Relational Mapping) API로, 데이터베이스와 객체 간의 매핑을 처리.
- Spring Data JPA는 JPA를 더 쉽게 사용할 수 있게 지원합니다.
- 주요 기능:
  - 엔티티(Entity)와 테이블 매핑.
  - JPQL(Java Persistence Query Language)을 사용한 쿼리.

---

### **영속성, Dirty Checking**

- **영속성(Persistence)**: JPA에서 엔티티가 영속성 컨텍스트에 의해 관리되는 상태.
- **Dirty Checking**: 영속성 컨텍스트는 엔티티의 상태 변화를 감지하고, 트랜잭션이 끝날 때 변경된 데이터를 자동으로 데이터베이스에 반영.

---

### **연관관계 (다대다 처리)**

- JPA에서 **다대다 관계**는 두 엔티티 간의 관계를 매핑합니다.
- **중간 테이블**을 사용해 다대다 관계를 효율적으로 처리.
- **예시**:
  java
  @Entity
  public class Student {
  @ManyToMany
  @JoinTable(name = "student_course",
  joinColumns = @JoinColumn(name = "student_id"),
  inverseJoinColumns = @JoinColumn(name = "course_id"))
  private List<Course> courses;
  }

### **JVM (Java Virtual Machine)**

#### **JVM 사용하는 이유**

1. **플랫폼 독립성**:
   - Java로 작성된 코드는 **바이트코드**로 컴파일되고, JVM이 바이트코드를 실행하므로
   - **Write Once, Run Anywhere** 를 실현.
1. **메모리 관리**:
   - JVM이 메모리 관리를 자동으로 수행(GC 사용)하여 개발자가 직접 메모리 해제를 신경 쓰지 않아도 됨.
1. **보안**:
   - JVM은 클래스 로더(Class Loader)와 바이트코드 검증을 통해 애플리케이션의 보안을 강화.
1. **성능 최적화**:
   - Just-In-Time Compiler(JIT)를 통해 런타임 시 기계 코드로 변환하여 실행 속도를 향상.
1. **풍부한 생태계**:
   - Java 생태계의 중심으로 다양한 라이브러리와 프레임워크를 지원.

---

### **JVM의 메모리 관리**

#### JVM 메모리 구조

1. **Method Area (메서드 영역)**:
   - 클래스 구조(메타데이터), 메서드, 상수 풀, static 변수 등을 저장.
2. **Heap Area (힙 영역)**:
   - 객체와 배열이 저장되는 메모리 영역. **GC(Garbage Collector)**가 관리.
3. **Stack Area (스택 영역)**:
   - 각 스레드가 사용하는 스택으로, 메서드 호출 시 생성되는 지역 변수와 호출 순서 관리.
4. **PC Register (프로그램 카운터 레지스터)**:
   - 각 스레드가 실행할 명령의 주소를 저장.
5. **Native Method Stack**:
   - 네이티브 코드(C 언어 등) 호출 시 사용.

---

### **GC (Garbage Collector)**

- **Garbage Collector**는 JVM에서 사용하지 않는 메모리를 자동으로 회수하는 역할.
- **작동 방식**:
  1. **Mark**: 참조되지 않는 객체를 식별.
  2. **Sweep**: 식별된 객체를 제거하여 메모리를 회수.
- **GC 종류**:
  - **Serial GC**: 단일 스레드로 동작.
  - **Parallel GC**: 다중 스레드로 처리.
  - **CMS GC**: 응답 속도를 높이기 위한 Low Latency GC.
  - **G1 GC**: 대규모 애플리케이션에 적합한 최신 GC.
- **GC의 장점**: 메모리 관리 자동화.
- **단점**: GC 실행 시 애플리케이션 성능 저하 가능(Stop-The-World 현상).

---

### **객체 지향 프로그래밍 (OOP, Object-Oriented Programming)**

#### **OOP란?**

- 현실 세계를 객체(Object)로 모델링하여 프로그래밍하는 방식.
- 객체는 **속성(데이터)**과 **행동(메서드)**로 구성.

#### **OOP의 장점**:

1. **코드 재사용**: 상속을 통해 기존 코드를 재사용 가능.
2. **유지보수성**: 코드 변경이 용이.
3. **확장성**: 새로운 기능 추가가 쉬움.

---

### **SOLID 원칙**

OOP 설계 원칙으로, 유지보수성과 확장성을 높이는 데 중점.

1. **Single Responsibility Principle (단일 책임 원칙)**:
   - 하나의 클래스는 하나의 책임만 가져야 함.
2. **Open/Closed Principle (개방/폐쇄 원칙)**:
   - 클래스는 확장에는 열려 있고, 변경에는 닫혀 있어야 함.
3. **Liskov Substitution Principle (리스코프 치환 원칙)**:
   - 서브 클래스는 부모 클래스의 기능을 대체할 수 있어야 함.
4. **Interface Segregation Principle (인터페이스 분리 원칙)**:
   - 인터페이스는 클라이언트에 맞게 분리되어야 함.
5. **Dependency Inversion Principle (의존 역전 원칙)**:
   - 상위 모듈은 하위 모듈에 의존하지 않아야 함(인터페이스를 통해 의존성 해결).

---

### **OOP의 4가지 특징**

1. **캡슐화 (Encapsulation)**:

   - 객체의 속성과 메서드를 하나로 묶고, 외부에서 접근을 제한.
   - **장점**: 데이터 보호 및 코드의 복잡성 감소.
   - **예시**:
     java
     코드 복사
     `public class User {     private String name; // 외부 접근 불가     public String getName() { return name; } // getter     public void setName(String name) { this.name = name; } // setter }`

2. **상속 (Inheritance)**:

   - 기존 클래스의 속성과 메서드를 자식 클래스가 물려받음.
   - **장점**: 코드 재사용성 증가.
   - **예시**:
     java
     코드 복사
     `class Animal {     void eat() { System.out.println("Eating"); } } class Dog extends Animal {     void bark() { System.out.println("Barking"); } }`

3. **다형성 (Polymorphism)**:

   - 하나의 메서드나 객체가 여러 형태를 가질 수 있음.
   - **오버로딩**: 같은 이름의 메서드를 매개변수로 구분.
   - **오버라이딩**: 부모 클래스의 메서드를 자식 클래스에서 재정의.
   - **예시**:
     java
     코드 복사
     `class Animal {     void sound() { System.out.println("Animal sound"); } } class Dog extends Animal {     @Override     void sound() { System.out.println("Bark"); } }`

4. **추상화 (Abstraction)**:

   - 불필요한 세부사항은 숨기고 중요한 정보만 제공.
   - **추상 클래스** 또는 **인터페이스**를 사용.
   - **예시**:
     java
     코드 복사
     `abstract class Shape {     abstract void draw(); // 추상 메서드 } class Circle extends Shape {     @Override     void draw() { System.out.println("Drawing Circle"); } }`

---

### **객체 지향 / 절차 지향**

| **객체 지향 프로그래밍**                      | **절차 지향 프로그래밍**      |
| --------------------------------------------- | ----------------------------- |
| 데이터와 메서드를 객체로 묶어 처리            | 작업을 순차적으로 처리        |
| 캡슐화, 상속, 다형성, 추상화 등 OOP 특징 적용 | 함수와 루프 기반의 프로그래밍 |
| 유지보수와 확장성이 뛰어남                    | 상대적으로 단순한 구조로 구현 |
| 예: Java, C++, Python                         | 예: C, Pascal                 |

---

### **N + 1 문제 해결**

- N + 1 문제는 JPA에서 발생하는 성능 문제로, 하나의 조회 쿼리에 대해 추가적인 N개의 쿼리가 실행되는 상황.
- 해결 방법:
  - **Fetch Join**: 연관된 엔티티를 한 번에 조회.
  - **Entity Graph**: `@EntityGraph`를 사용해 필요한 연관 엔티티를 함께 조회.
  - **Lazy Loading 최적화**: 지연 로딩 전략 조정.

---

### **DB (Database)**

- 데이터를 저장하고 관리하는 시스템으로, RDBMS(MySQL, PostgreSQL)와 NoSQL(MongoDB 등)로 나뉩니다.

---

### **Index**

- 데이터베이스에서 데이터 검색 속도를 높이기 위해 사용.
- **종류**:
  - 기본 인덱스 (Primary Key).
  - 보조 인덱스 (Secondary Index).

---

### **Unique**

- 특정 컬럼에 중복된 값이 저장되지 않도록 보장하는 제약 조건.

---

### **SQL**

- Structured Query Language로 데이터베이스와 상호작용.
- 주요 명령어:

  - **DDL**: CREATE, ALTER, DROP.
  - **DML**: SELECT, INSERT, UPDATE, DELETE.
  - **DCL**: GRANT, REVOKE.
  - **TCL**: COMMIT, ROLLBACK. **SAVEPOINT**, SET TRANSACTION

- ### **DDL (Data Definition Language)**

데이터베이스의 구조를 정의하거나 변경하는 명령어입니다.

- **CREATE**: 테이블, 인덱스, 뷰, 스키마 등을 생성.
  `CREATE TABLE users ( id INT PRIMARY KEY, name VARCHAR(50) );`
- **ALTER**: 기존 객체(테이블 등)의 구조를 변경.
  `ALTER TABLE users ADD email VARCHAR(100);`
- **DROP**: 테이블, 뷰, 스키마 등 삭제.

  `DROP TABLE users;`

---

### **DML (Data Manipulation Language)**

데이터베이스 내 데이터를 조작하는 데 사용됩니다.

- **SELECT**: 데이터를 조회.
  `SELECT * FROM users WHERE id = 1;`
- **INSERT**: 데이터를 삽입.
  `INSERT INTO users (id, name) VALUES (1, 'John Doe');`
- **UPDATE**: 기존 데이터를 수정.
  `UPDATE users SET name = 'Jane Doe' WHERE id = 1;`
- **DELETE**: 데이터를 삭제.
  `DELETE FROM users WHERE id = 1;`

---

### **DCL (Data Control Language)**

데이터베이스의 권한을 제어하는 명령어입니다.

- **GRANT**: 사용자에게 권한 부여.
  `GRANT SELECT, INSERT ON users TO 'username';`
- **REVOKE**: 권한 취소.
  `REVOKE INSERT ON users FROM 'username';`

---

### **TCL (Transaction Control Language)**

트랜잭션을 제어하는 명령어입니다. 트랜잭션은 데이터베이스에서 하나의 논리적 작업 단위로, 데이터의 일관성을 보장합니다.

- **COMMIT**: 트랜잭션 작업 내용을 확정(영구적으로 저장).
  `COMMIT;`
- **ROLLBACK**: 트랜잭션 작업 내용을 취소(변경 사항을 되돌림).
  `ROLLBACK;`
- **SAVEPOINT**: 트랜잭션 내 특정 지점을 설정해 부분적인 ROLLBACK 가능.
  `SAVEPOINT save1;`
- **SET TRANSACTION**: 트랜잭션의 속성을 설정(예: 격리 수준).
  `SET TRANSACTION ISOLATION LEVEL READ COMMITTED;`

---

### **SQL 명령어 간 관계**

1. **DDL** 명령어 실행 시 자동으로 COMMIT 수행(ROLLBACK 불가).
2. **DML** 명령어는 명시적으로 COMMIT이나 ROLLBACK을 호출해야 트랜잭션 종료.
3. **TCL**은 DML 명령어와 함께 주로 사용되며 데이터의 무결성을 보장.

---

### **파티셔닝(Partitioning)**

- 큰 데이터를 나눠 관리해 성능을 향상시키는 기법.
- 종류:
  - **Range Partitioning**: 범위 기준.
  - **Hash Partitioning**: 해시 값을 기준.

---

### **샤딩(Sharding)**

- 데이터를 여러 데이터베이스에 분산 저장해 확장성과 성능을 향상.
- 예: 사용자를 ID 기준으로 분리.
