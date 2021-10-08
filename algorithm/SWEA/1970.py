# 1970 쉬운 거스름돈
coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
def dfs(now, index, cnt=0):
    # 지금 남은 돈,
    global min_cnt, ans
    if now < 10:
        if cnt < min_cnt:
            min_cnt = cnt
            ans = path[:]
        return

    for i in range(index, len(coins)):
        k = now // coins[i]
        if k > 0:
            path[i] = k
            dfs(now - k*coins[i], i + 1, cnt+k)
            path[i] = 0

T = int(input())
for tc in range(T):
    # 거슬러 줘야하는 돈
    N = int(input().rstrip())
    min_cnt = N
    path = [0] * len(coins)
    ans = [0] * len(coins)
    dfs(N, 0)

    print(f'#{tc + 1}')
    print(*ans)


