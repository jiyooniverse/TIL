# 13040 전자카트
def dfs(now, total, cnt):
    global ans
    if cnt > N and now == 0:
        if ans > total:
            ans = total
        return

    for next in range(N):
        if next == now:
            continue

        if check[next] == 0:
            check[next] = 1
            dfs(next, total + MAP[now][next], cnt + 1)
            check[next] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N

    ans = 9876543210
    dfs(0, 0, 1)

    print(f'#{tc + 1} {ans}')

