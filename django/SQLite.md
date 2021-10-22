# SQLite

`SQLite`는 데이터베이스 관리 시스템 중 하나로 기본적으로 `django`에서 사용가능 하도록 설정되어 있으며 서버가 아니라 응용 프로그램에 넣어 사용하여 가벼운 데이터베이스이다.



- 데이터베이스 생성

  기존에 <databasename>의 db가 있으면 해당 db에 연결한다.
  
  ```bash
  $ sqlite3 <databasename>.sqlite3
  ```
  
  > <databasename> 없이 `sqlite3`만 실행 시 **Connected to a trasient in-memory database** → database에 저장되지 않음 .



데이터베이스 생성문 실행 후 `sqlite` 프롬프트 환경으로 설정된다. (`sqlite`가 프롬프트 앞에 붙음)

SQLite는 사용자가 SQLite 데이터베이스에 대해 수동으로 SQL문을 실행할 수 있도록 하는 간단한 명령어들에 대해 제공한다. 이를 `sqlite dot(.) command`라 한다.

- 데이터베이스 확인

  ```sqlite
  .database
  ```

- sqlite 프롬프트에서 나오기

  ```sqlite
  .quit
  ```

- `csv` 파일 데이터 database에 넣기

  ```sqlite
  .mode csv
  .import example.csv examples
  ```

- DB의 `table` 확인하기

  ```sqlite
  .tables
  ```

- table의 `schema` 확인하기

  ```sqlite
  .schema classmates
  ```

- terminal 환경에서 환경 설정

  ```sqlite
  .headers on
  .mode column
  ```





# SQL ORM

- ORM(object-Relation Mapping)은 객체지향 프로그래밍 언어와 관계형 데이터 베이스를 연결해주는 방법이다.

  > Python --> ORM --> Database

- Django 프레임워크에서는 기본적으로 `ORM`을 제공하고 있다.



- shell_plus를 통해 실습하기

  ```bash
  $ python manage.py shell_plus
  ```

  > DB에 테스트로 데이터를 생성하거나 다룰 때 shell을 통해 간편하게 작업할 수 있다.
  
- SQL ORM

  - all()
  - get()
  - filter()
    - `__lte`, `__gte` ,`__lt`, `__gt` 
    - `__endswith`, `__startswith`
    - or --> Q 사용
  - values()
  - order_by()
  - distinct()
  - aggregate()
    - `Max()`, `Avg`, `Min`, ...
  - SQL 질의문 확인하기 str(queryset.query





