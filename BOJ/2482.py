# BOJ 2482 색상환
# n색상환에서 인접한 색 뽑지 않고 k개 고를 수 있는 경우의 수
n = int(input())
k = int(input())

# dp[몇개의 색 중에서][고른색의 수]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1
    dp[i][1] = i
for i in range(2, n):
    for j in range(2, k + 1):
        if i < j:
            break
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 2][j - 1]

ans = (dp[n-1][k] + dp[n-3][k-1]) % 1000000003
print(ans)
