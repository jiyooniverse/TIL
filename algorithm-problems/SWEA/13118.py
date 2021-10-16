# 13118 전기버스 2
def dfs(now):
    global min_cnt
    # 종점 지나는 곳에서 0 반환
    if now >= N - 1:
        return 0

    if dp[now] != -1:
        return dp[now]

    ret = N
    for j in range(bus[now], 0, -1):
        # now에서 bus[now]까지 갈 수 있다
        ret = min(ret, dfs(now + j) + 1)

    dp[now] = ret
    return ret



T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    N = arr[0]
    bus = arr[1:]
    dp = [-1] * N

    dfs(0)
    # 마지막 정류장 빼주기
    print(f'#{tc + 1} {dp[0] - 1}')
