# SWEA 파리 퇴치
T = int(input())

for test_case in range(T):
    n, m = map(int, input().split())
    # n*n 크기의 맵 input으로 들어오면
    # m*m 크기만큼 돌며 값 더하기
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_fly = 0
    for i in range(n+1-m):
        for j in range(n+1-m):
            tmp_fly = 0
            for k in range(m):
                for l in range(m):
                    tmp_fly += arr[i+k][j+l]
            if tmp_fly > max_fly:
                max_fly = tmp_fly

    print(f"#{test_case + 1} {max_fly}")

# SWEA 파리채 문제 DP 이해하기
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     MAP = [[0 for _ in range(N + 1)]]
#     for i in range(N):
#         MAP += [[0] + list(map(int, input().split()))]
#     dp = [[0] * (N + 1) for _ in range(N + 1)]
# 
#     for row in range(1, N + 1):
#         for col in range(1, N + 1):
#             dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + MAP[row][col]
# 
#     ans = 0
#     for row in range(M, N + 1):
#         for col in range(M, N + 1):
#             sum = dp[row][col] - dp[row - M][col] - dp[row][col - M] + dp[row - M][col - M]
#             if ans < sum:
#                 ans = sum
# 
#     print("#{} {}".format(tc + 1, ans))
