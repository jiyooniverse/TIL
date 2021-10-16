# SUM, MAX, MIN

1. 최댓값 구하기

   ```mysql
   SELECT MAX(DATETIME) FROM ANIMAL_INS
   ```

2. 최솟값 구하기

   ```mysql
   SELECT MIN(DATETIME) FROM ANIMAL_INS
   ```

3. 동물 수 구하기

   ```mysql
   SELECT COUNT(*) FROM ANIMAL_INS
   ```

4. 중복 제거하기

   ```mysql
   SELECT COUNT(DISTINCT(NAME)) FROM ANIMAL_INS
   ```

   