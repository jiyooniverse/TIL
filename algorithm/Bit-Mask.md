# 비트 마스크(Bit Mask)

비트(bit)란 정보를 처리하는 데이터의 최소 단위로 하나의 비트는 `0` 또는  `1`값을 가지며 모든 데이터는 `0`과 `1`의 조합으로 구성된다. 

- 비트 연산
  - `&` : AND

    - i & (1<<j)하면 i의 j번 비트 1인지 확인.

      > (1<<j)하면 나머지 비트는 모두 0이므로 나머지 위치는 다 0이고 i의 j번째만 이제 확인.

  - `|` : OR

    - i | (1<<j)하면 i의 j번 비트를 무조건 1로 변경.

  - `^` : 같으면 0 다르면 1

    - 1 << j 하고 num과 `^` 하면 j번째만 반대로 나옴.

      >  j번째만 1이고 나머지는 0. num하고 `^` 하면 num에서 원래 0인 비트는 0나오고 1이면 다르니까 1나오고, j번째가 원래 0이면 다르니까 1나오고 원래 1이면 같으니까 0나옴.

  - `~` : 모든 비트 반전

  - `<<` : 비트 열을 왼쪽으로 이동

  - `>>` : 비트 열 을 오른쪽으로 이동



- 활용
  - 부분집합

    ```python
    # n = len(arr)
    for i in range(0, (1<<n)):	# 부분집합 개수
        for j in range(0, len(arr)):	# 원소의 수만큼 비트 비교
            # j번째 비트(원소)가 포함인지 아닌지
            if i & (1<<j):
                print(arr[j])
        print()     
    ```

    > 부분집합 개수 1 ~ 2**n개를 비트로 표현하면, 0, 1, 10, 11, 100, 101, 110, ... 이 되므로 i와 j를 `&` 연산 하면 j번째 원소 포함인지 아닌지 확인 가능(0이면 불포함, 0이 아니면 j번째 index 포함됨)

  - mask 생성

    ```python
    mask = (1 << n) - 1
    # 1111....111 : 길이 n인 mask 생성
    ```

  

----

- 관련 문제
  - [외판원 순회](https://www.acmicpc.net/problem/2098)

    - [풀이](https://github.com/jiyooniverse/TIL/blob/master/algorithm-problems/BOJ/2098.py)

  - [폰트](https://www.acmicpc.net/problem/9997)

    - [풀이](https://github.com/jiyooniverse/TIL/blob/master/algorithm-problems/BOJ/9997.py)

    

