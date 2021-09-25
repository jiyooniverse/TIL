# SQLite

`SQLite`는 데이터베이스 관리 시스템 중 하나로 기본적으로 `django`에서 사용가능 하도록 설정되어 있으며 서버가 아니라 응용 프로그램에 넣어 사용하여 가벼운 데이터베이스이다.



- 데이터베이스 생성

```sqlite
$ sqlite3 <databasename>.sqlite3
```

데이터베이스 생성문 실행 후 `sqlite` 프롬프트 환경으로 설정된다. (`sqlite`가 프롬프트 앞에 붙음 )

- 데이터베이스 확인

```sqlite
sqlite>.database
```

- sqlite 프롬프트에서 나오기

```sqlite
sqlite>.quit
```





```sqlite
.mode csv
.import example.csv examples
.tables
SELECT * FROM examples
.headers on
.mode column
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
    name TEXT
);
.schema classmates
DROP TABLE classmates;

```





### Migrate





### SQL ORM

