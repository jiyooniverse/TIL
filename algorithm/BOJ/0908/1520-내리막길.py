# BOJ 1520 내리막길 # PyPy3로 실행
import sys
M, N = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[0] * N for _ in range(M)]
check = [[0] * N for _ in range(M)]
# 0,0에서부터 시작
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dp[0][0] = 1
def dfs(r, c):
    check[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N \
                and MAP[nr][nc] > MAP[r][c]:
            if check[nr][nc] == 1:
                dp[r][c] += dp[nr][nc]
            else:
                dp[r][c] += dfs(nr, nc)
    return dp[r][c]
dfs(M-1, N-1)
print(dp[M-1][N-1])