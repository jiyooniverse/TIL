# 13037 최소합
# 오른쪽, 아래쪽
dr = [0, 1]
dc = [1, 0]

def dfs(now, total):
    global ans
    r = now[0]
    c = now[1]

    if r == N - 1 and c == N - 1:
        # 오른쪽 아래 도착
        if ans > total:
            ans = total
        return

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < N and nc < N:
            if dp[nr][nc] == 0 or dp[r][c] + MAP[nr][nc] < dp[nr][nc]:
                dp[nr][nc] = dp[r][c] + MAP[nr][nc]
                dfs([nr, nc], total + MAP[nr][nc])


T = int(input())
for tc in range(T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # dp로도 풀어보기
    dp = [[0] * N for _ in range(N)]
    ans = 10000
    dp[0][0] = MAP[0][0]
    dfs([0, 0], MAP[0][0])

    # print(f'#{tc + 1} {ans}')
    print(f'#{tc + 1} {dp[N-1][N-1]}')
