# 2. 부분집합의 합
for test_case in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    result_count = 0
    for i in range(1<<N): # 부분집합의 총개수는 2^n : 이진수로 표현
        temp = 0
        for j in range(N):    # j번째 원소의 bit가 0/1 인지
            if i & (1<<j):    # i는 십진수이지만 이진수로 변경하면 각 원소의 유무를 0/1로 표현한것이라 할 수 있다.
                de = arr[j]                # (1<<j)는 j라는 수를 이진수로 표현한 것이라 할 수 있므.
                temp += arr[j]
        if temp == 0:
            result_count += 1

    print(f'#{test_case + 1} {result_count}')