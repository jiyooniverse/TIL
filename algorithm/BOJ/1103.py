# 1103 게임
import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
board = [list(str(input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
check = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]

def dfs(now, cnt=1):
    global ans
    if ans == -1:
        return
    r = now[0]
    c = now[1]
    X = int(board[r][c])

    for i in range(4):
        if ans == -1:
            return
        # 상하좌우 방향으로 X 만큼 이동
        nr = r + dr[i] * X
        nc = c + dc[i] * X
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 'H' and dp[nr][nc] < cnt + 1:
            # 보드 범위 안에 있고 움직일 곳이 hole이 아니면 또 한다.
            # 다시 나에게 올 수 있으면 무한대이므로 -1 출력
            if check[nr][nc] != 0:
                ans = -1
                return
            dp[nr][nc] = cnt + 1
            check[nr][nc] = 1
            dfs([nr, nc], cnt + 1)
            check[nr][nc] = 0

        else:
            if ans != -1 and ans < cnt:
                ans = cnt


ans = 0
check[0][0] = 1
dfs([0, 0])
print(ans)



