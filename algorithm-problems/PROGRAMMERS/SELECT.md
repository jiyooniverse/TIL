# SELECT

1. 모든 레코드 조회하기

   ```mysql
   SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID
   ```

2. 역순 정렬하기

   ```mysql
   SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC
   ```

3. 아픈 동물 찾기

   ```mysql
   SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = 'Sick'
   ```

4. 어린 동물 찾기

   ```mysql
   SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONTION != 'Aged' ORDER BY ANIMAL_ID
   ```

5. 동물의 아이디와 이름

   ```mysql
   SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID
   ```

6. 여러 기준으로 정렬하기

   ```mysql
   SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME ASC, DATETIME DESC
   ```

7. 상위 n개 레코드

   ```mysql
   SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1
   ```

   