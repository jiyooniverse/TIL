# SWEA 부분집합의 합
T = int(input())
total_set = list(range(1, 13))  # 1 ~ 12를 원소로 가지는 집합
for test_case in range(T):
    n, k = map(int, input().split())
    result = 0
    # total_set에서 n개만 뽑기
    for i in range(1<<len(total_set)):
        set_count = 0
        set_sum = 0
        for j in range(len(total_set)):
            if i & (1<<j):
                set_count += 1
                set_sum += total_set[j]

        if set_count != n:
            continue

        # 원소가 3개이면 set_sum이 k개인지 확인
        if set_sum == k:
            result += 1

    print(f"#{test_case + 1} {result}")