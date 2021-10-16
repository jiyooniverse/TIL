# sum
T = 10

for test_case in range(T):
    n = int(input())
    # 100 * 100 2차원 행렬
    arr = [list(map(int, input().split()) )for i in range(100)]

    max_sum = 0
    # 각 행의 합
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            temp_sum += arr[i][j]
        if max_sum < temp_sum:
            max_sum = temp_sum
    # 각 열의 합
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            temp_sum += arr[j][i]
        if max_sum < temp_sum:
            max_sum = temp_sum
    # 대각선 합 1
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            if i == j:
                temp_sum += arr[i][j]
        if max_sum < temp_sum:
            max_sum = temp_sum

    # 대각선 합 2
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            if j == (len(arr) - 1):
                temp_sum += arr[i][j]
        if max_sum < temp_sum:
            max_sum = temp_sum

    print(f"#{test_case + 1} {max_sum}")