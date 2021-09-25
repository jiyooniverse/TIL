# BOJ 1149 RGB 거리
n = int(input())    # 집의 수
rgb = [list(map(int, input().split())) for _ in range(n)]

# i번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# dp[색][집 수]
dp = [[0] * 3 for _ in range(n)]
dp[0] = rgb[0]
for i in range(1, n):
    # 이전 최적값이 있을 때, index 값과 겹치지 않는 cost 중 작은 값을 넣어준다.
    for c in range(3):
        if dp[i - 1][(c + 1) % 3] < dp[i - 1][(c + 2) % 3]:
            dp[i][c] = dp[i - 1][(c + 1) % 3] + rgb[i][c]
        else:
            dp[i][c] = dp[i - 1][(c + 2) % 3] + rgb[i][c]


print(min(dp[n-1]))